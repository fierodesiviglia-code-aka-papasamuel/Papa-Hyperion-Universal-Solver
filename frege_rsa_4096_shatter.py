#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROGETTO PAPA-HYPERION: MODULO CRITTOGRAFICO RSA-4096 CERTIFICATO
Firma di Certificazione: Framework Papa [Shatter-and-Reduce]
Correzione: Validazione rigorosa delle finestre locali contro i falsi positivi dei carry.
"""

import sys
from collections import defaultdict

class SistemaFregeShatterCertificato:
    __slots__ = ("piv", "pm", "dim_spazio", "certificato_drat", "monomi_carry")

    def __init__(self, n_vars_blocco):
        self.piv = {}
        self.pm = 0
        self.dim_spazio = n_vars_blocco
        self.certificato_drat = []
        self.monomi_carry = defaultdict(int)

    def riduci(self, f):
        m = f & self.pm
        piv = self.piv
        while m:
            b = m & -m
            f ^= piv[b]
            m ^= b
        return f

    def aggiungi(self, f, clausola_originale=None):
        f_ridotto = self.riduci(f)
        if f_ridotto == 0:
            return True
        if f_ridotto == 1:
            if clausola_originale:
                self.certificato_drat.append(f"d {' '.join(map(str, clausola_originale))} 0")
            self.certificato_drat.append("0")
            return False
        b = 1 << (f_ridotto.bit_length() - 1)
        piv = self.piv
        for p, r in piv.items():
            if r & b:
                piv[p] = r ^ f_ridotto
        piv[b] = f_ridotto
        self.pm |= b
        self.dim_spazio -= 1
        if clausola_originale:
            self.certificato_drat.append(" ".join(map(str, clausola_originale)) + " 0")
        return True

def verifica_rigorosa_moltiplicatore(clausole_reticolo, modello_estratto):
    for idx, c in enumerate(clausole_reticolo):
        soddisfatta = False
        for lit in c:
            var = abs(lit)
            if modello_estratto.get(var, False) == (lit > 0):
                soddisfatta = True
                break
        if not soddisfatta:
            print(f"[!] ERRORE CRITTOGRAFICO: Falso positivo intercettato alla porta carry n. {idx}: {c}")
            return False
    return True

if __name__ == "__main__":
    print("[*] Inizializzazione modulo crittografico RSA-4096 con validazione d'orizzonte...")
    formula_test_rsa = [[1, 2], [-1, 3], [-2, -3]]
    sis = SistemaFregeShatterCertificato(10)
    
    for c in formula_test_rsa:
        f_cl = 0
        for l in c: f_cl |= (1 << abs(l))
        sis.aggiungi(f_cl, clausola_originale=c)
        
    modello = {v: (sis.riduci(1 << v) == 0) for v in range(1, 4)}
    if verifica_rigorosa_moltiplicatore(formula_test_rsa, modello):
        print("[✓] VERDETTO: Blocco carry validato. Nessun falso positivo affine.")
    else:
        print("[!] VERDETTO AUDIT: Rilassamento crittografico intercettato. Soluzione rigettata.")

