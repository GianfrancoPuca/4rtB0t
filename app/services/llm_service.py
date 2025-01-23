from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="unsloth/phi-4-GGUF",
    filename="phi-4-F16.gguf",
)

def generate_response(user_message):
    response = llm.create_chat_completion(
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    return response["choices"][0]["message"]["content"]
