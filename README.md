# Artbot

Questo progetto è un chatbot avanzato progettato per rispondere a domande su come enfatizzare e sviluppare aspetti delle mostre d'arte. Il chatbot utilizza modelli linguistici open source, tra cui Mistral, e una documentazione caricata su Google Drive come base di conoscenza.

## Scopo del Progetto
L'obiettivo principale di questo progetto è facilitare l'accesso alle informazioni relative alla gestione, alla progettazione e allo sviluppo di mostre d'arte. Attraverso un'interfaccia semplice e intuitiva, gli utenti possono ottenere risposte dettagliate basate sulla documentazione fornita.

## Funzionalità
- **Risposte basate su documentazione**: il chatbot analizza e fornisce risposte basate sui documenti caricati su Google Drive.
- **Riconoscimento di contesto**: utilizza embedding semantici per individuare i contenuti più pertinenti.
- **Generazione di linguaggio naturale**: risposte fluide e contestualizzate generate da Mistral.

## Tecnologie Utilizzate
- **Linguaggi e framework**: Python, Flask
- **Modelli di machine learning**:
  - Mistral per la generazione di risposte.
  - SentenceTransformers per il calcolo degli embedding.
- **Integrazione con servizi esterni**:
  - API di Google Drive per il caricamento e l'accesso ai documenti.
  - Hugging Face per l'accesso ai modelli pre-addestrati.
- **Elaborazione dei documenti**: pdfplumber per estrarre il testo dai PDF.

## Requisiti Tecnici
- Python 3.8 o superiore
- Dipendenze elencate in `requirements.txt`
- Account Google con accesso ai file richiesti
- Token Hugging Face per accedere ai modelli

## Istruzioni per l'Installazione

### Passaggi per la configurazione locale
1. **Clonare il repository**:
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. **Creare un ambiente virtuale**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # Su Windows: env\Scripts\activate
   ```

3. **Installare le dipendenze**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurare le credenziali di Google Drive**:
   - Posizionare il file `secrets.json` nella directory `config/`.

5. **Impostare variabili d'ambiente**:
   - Creare un file `.env` con il seguente contenuto:
     ```env
     huggingface_token=<IL_TUO_TOKEN>
     ```

6. **Avviare l'applicazione**:
   ```bash
   python main.py
   ```

## Utilizzo del Chatbot

### Esempio di Sessione
```plaintext
Utente: Come posso migliorare l'illuminazione per una mostra?
Chatbot: L'illuminazione dovrebbe essere regolata in base al tipo di opere esposte. Ad esempio, le opere su tela richiedono luce diffusa per evitare riflessi.
```

## Struttura delle Cartelle
```plaintext
repository-name/
├── config/
│   └── secrets.json          # Credenziali per l'accesso a Google Drive
├── data/
│   ├── raw/                  # Documenti grezzi scaricati
│   ├── processed/            # Documenti preprocessati
│   └── embeddings/           # Embedding generati
├── logs/                     # File di log per monitorare il preprocessing
├── app/
│   ├── routes.py             # Gestione delle route Flask
│   └── templates/            # Template HTML (se applicabile)
├── main.py                   # Entrypoint principale dell'applicazione
├── preprocessing.py          # Script per preprocessare i documenti
├── mistral_service.py        # Integrazione con il modello Mistral
├── embedding_service.py      # Gestione degli embedding
├── drive_service.py          # Integrazione con Google Drive
├── requirements.txt          # Dipendenze del progetto
└── README.md                 # Documentazione del progetto
```

## Contributi

Siamo aperti ai contributi! Segui questi passaggi per proporre miglioramenti:
1. Fai un fork del repository.
2. Crea un branch per la tua feature o correzione:
   ```bash
   git checkout -b feature-nome-feature
   ```
3. Effettua le modifiche e scrivi commit descrittivi.
4. Invia una pull request.

## Limiti Noti
- Il chatbot richiede una connessione a Internet per accedere alle API di Google Drive e Hugging Face.
- Le risposte dipendono dalla qualità e dalla pertinenza della documentazione caricata.

## Estensioni Future
- Supporto per altre lingue oltre all'italiano.
- Integrazione con più sorgenti di documentazione, come database SQL.
- Implementazione di un'interfaccia web più avanzata.

## Riferimenti
- [API di Google Drive](https://developers.google.com/drive)
- [Mistral LLM](https://mistral.ai)
- [SentenceTransformers](https://www.sbert.net)

---
Sentiti libero di contattarmi per eventuali domande o suggerimenti! 😊

