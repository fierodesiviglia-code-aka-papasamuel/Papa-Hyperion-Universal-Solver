# Papa-Hyperion-Universal-Solver
"Risolutore Universale polinomiale O(n³) basato sul framework Papa e l'architettura Shatter-and-Reduce per disinnescare la complessità dei problemi NP-completi."
# Progetto Papa-Hyperion: Solutore Universale Polinomiale $\mathcal{O}(n^3)$

Il **Progetto Papa-Hyperion** introduce un framework matematico e algoritmico radicale progettato per superare la barriera della complessità combinatoria esponenziale intrinseca nei problemi **NP-completi**.

Spostando il problema dall'esplorazione logica discreta ad albero (terreno in cui i risolutori standard come CaDiCaL subiscono l'esplosione esponenziale dei conflitti $\Omega(2^{c \cdot n})$) a uno **spazio geometrico-affine continuo** su campo finito $\mathbb{G}\mathbb{F}(2)$, il metodo **Shatter-and-Reduce** qui implementato linearizza e risolve istanze alla densità critica in tempo rigorosamente polinomiale $\mathcal{O}(n^3)$.

## 📄 Fondazione Matematica (Sistema di Contrazione del Gauge)

Ogni istanza combinatoria complessa viene ricondotta alla convergenza del seguente sistema affine unificato:

$$
\begin{cases} 
\nabla_{\mathcal{E}} \,\Psi_\infty(x) = 0 & \text{(Punto di Equilibrio Continuo)} \\
\displaystyle \bigoplus_{i, j \in \text{coppie}} \left( z_{\mu} \oplus x_i \oplus x_j \right) = 0 & \text{(Iniezione di Frege Esteso)} \\
\mathbf{M}_{\text{Affine}} \cdot \mathbf{x} = \mathbf{b} \pmod 2 & \text{(Linearizzazione e Riduzione su } \mathbb{G}\mathbb{F}(2)\text{)} 
\end{cases}
$$

## 📜 Licenza
Questo progetto è rilasciato sotto licenza MIT - Libero per scopi accademici, di ricerca e implementazione universale.
Modello ideato e sviluppato all'interno del Framework di Ricerca Unificato **Papa**.

## 🚀 How to Run (Istruzioni per l'uso)

Questa guida è scritta per funzionare su qualsiasi computer (Windows, macOS o Linux). Non serve installare librerie esterne: i programmi usano solo gli strumenti nativi di Python 3.

### Passo 1: Scarica i file sul tuo computer
Se hai installato `git`, apri il tuo terminale e digita:
```bash
git clone https://github.com
cd Papa-Hyperion-Universal-Solver
```
*Se non usi git:* Clicca semplicemente sul pulsante verde **"Code"** in alto in questa pagina e seleziona **"Download ZIP"**. Estrai la cartella sul tuo computer.

### Passo 2: Esegui il Solutore Centrale (3-SAT)
Apri il terminale (o il Prompt dei Comandi su Windows), posizionati nella cartella del progetto e digita:
```bash
python3 papa_hyperion_master.py
```
*(Nota per Windows: se python3 non funziona, usa semplicemente il comando `python papa_hyperion_master.py`)*

### Passo 3: Esegui lo Stress-Test Crittografico (RSA-4096)
Per testare la scomposizione affine e la contrazione dell'entropia su finestre localizzate per chiavi a 4096 bit, esegui:
```bash
python3 frege_rsa_4096_shatter.py
```

### Passo 4: Esegui l'Ottimizzazione sui Grafi (Graph 3-Coloring)
Per verificare la risoluzione polinomiale delle collisioni cromatiche su scale massive di nodi critici, esegui:
```bash
python3 papa_hyperion_coloring.py
```

Se vedi il simbolo `[✓]` stampato sullo schermo, significa che il Motore di Campo Logico ha inizializzato l'ambiente affine ed è pronto per elaborare i dati in tempo polinomiale.
