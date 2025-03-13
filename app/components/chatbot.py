from llama_cpp import Llama

MODEL_PATH = "C:/Users/deyna/Desktop/air-quality/models/llama-2-7b.Q4_K_M.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,  # Increase context size for better answers
    n_threads=6,  # Adjust based on CPU cores (more = faster)
    verbose=False  # Prevents unnecessary logs
)

def ask_bot(question):
    # Generate a clear and short response without unnecessary sub-options
    if not question.strip():
        return "Please enter a valid question."

    prompt = f"""You are an environmental science expert. Provide a **concise, straightforward, and direct** answer.
    
    Do **not** list multiple options unless explicitly asked.

    Question: {question}
    Answer:"""

    try:
        response = llm(prompt, max_tokens=200, temperature=0.2, top_p=0.9, stop=["\n\n", "Option:", "•", "○"])
        return response["choices"][0]["text"].strip()
    except Exception as e:
        return f"⚠️ Error generating response: {str(e)}"

