# ArtBot

ArtBot è un chatbot progettato per rispondere a domande riguardo l’organizzazione, la progettazione e la valorizzazione di **mostre d’arte**. Sfrutta modelli di **machine learning** open source e una base di conoscenza caricata da documenti PDF per fornire risposte contestuali e mirate.

---

## Indice
1. [Scopo del Progetto](#scopo-del-progetto)
2. [Funzionalità](#funzionalità)
3. [Struttura del Progetto](#struttura-del-progetto)
4. [Requisiti Tecnici](#requisiti-tecnici)
5. [Installazione e Avvio](#installazione-e-avvio)
6. [Utilizzo](#utilizzo)

---

## Scopo del Progetto
- **Facilitare l’accesso alle informazioni** riguardanti mostre d’arte (allestimenti, illuminazione, comunicazione, budget, ecc.).
- **Fornire un’interfaccia semplice e intuitiva** per ottenere risposte rapide su temi artistici e museali.

---

## Funzionalità
1. **Analisi dei documenti**: indicizzazione di PDF (o altre fonti) con strumenti di Embedding (es. *SentenceTransformers*) e un indice FAISS (o simile) per recuperare i contenuti più pertinenti.  
2. **Generazione di testo naturale**: ArtBot si appoggia a modelli LLM (es. *Mistral*, *Hugging Face*) per restituire risposte fluenti.  
3. **Interfaccia web**: include un frontend minimal in *Flask + JS*, con supporto alla Dark Mode e design *mobile-friendly*.  
4. **Feedback opzionale**: possibilità di fornire feedback (👍/👎) sulle risposte per una valutazione futura.

---

## Struttura del Progetto

```plaintext
artbot/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── services/
│   │   ├── llm_service.py
│   │   └── ...
│   ├── templates/
│   │   └── index.html          # Pagina HTML principale del chatbot
│   └── static/
│       ├── style.css           # Stili CSS (light/dark)
│       ├── script.js           # Logica frontend (fetch, dark mode, UI)
│       └── imgs/               # Eventuali immagini o icone
├── data/
│   ├── raw/                    # Documenti PDF originali
│   └── processed/              # Documenti .txt preprocessati
├── config/                     # (Opzionale) Credenziali .json per Google Drive, file .env
├── run.py                      # Avvio dell’app Flask (create_app e app.run)
├── requirements.txt            # Dipendenze
├── .gitignore                  # Voci da ignorare (venv310, .env, ecc.)
└── README.md                   # Documentazione del progetto

Requisiti Tecnici
Python 3.10 (consigliato, visti i requisiti di PyTorch e librerie correlate)

Connettività a Internet (se utilizzi modelli e servizi esterni, come Hugging Face o Google Drive)
Librerie installate da requirements.txt

Installazione e Avvio
Clona il repository:

git clone https://github.com/username/artbot.git
cd artbot

Crea un ambiente virtuale (es. venv310):

python3.10 -m venv venv310
source venv310/bin/activate  # (Su Windows: venv310\Scripts\activate)

Installa le dipendenze:

pip install --upgrade pip
pip install -r requirements.txt

(Facoltativo) Configura Google Drive:

Se devi scaricare PDF da Drive, inserisci le tue credenziali (client_secrets.json) in config/.
Imposta eventuali variabili d’ambiente (es. ID di cartelle Drive, token, ecc.).

Avvia l’applicazione:

python run.py
Il server girerà di default su http://127.0.0.1:5000/.

Utilizzo

Interfaccia Web: Apri http://127.0.0.1:5000/ nel tuo browser per accedere al chatbot.

Modalità Dark: Clicca sull’icona “dark_mode” nella barra superiore per passare dalla modalità chiara a quella scura.

Conversazione: Digita la tua domanda o richiesta nel box di input e premi Invio o clicca sull’icona di invio.

Feedback (opzionale): Se implementato, appariranno emoji 👍/👎 per valutare la pertinenza della risposta.