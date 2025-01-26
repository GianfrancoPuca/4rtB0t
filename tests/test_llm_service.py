from llama_cpp import Llama

try:
    llm = Llama.from_pretrained(
        repo_id="unsloth/phi-4-GGUF",
        filename="models/phi-4-F16.gguf",
    )
    print("Modello caricato con successo!")
except Exception as e:
    print(f"Errore durante il caricamento del modello: {e}")

