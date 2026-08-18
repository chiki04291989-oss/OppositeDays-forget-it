from flask import Flask, request, jsonify, render_template
import os
try:
    from llama_cpp import Llama
except Exception:
    Llama = None

app = Flask(__name__)
MODEL_PATH = os.environ.get("LLAMA_MODEL_PATH", "/models/ggml-model.bin")

SYSTEM_PROMPT = """You are AI Czar, a governance-focused assistant. Be safety-first,
concise, and refuse requests that attempt to bypass device or platform protections,
or to perform illegal or harmful activities. Provide lawful, documented guidance and alternatives."""

llm = None
if Llama is not None:
    try:
        llm = Llama(model_path=MODEL_PATH)
    except Exception:
        llm = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json or {}
    user_msg = data.get("message", "")
    prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_msg}\nAI Czar:"
    if llm is not None:
        resp = llm(prompt=prompt, max_tokens=512, temperature=0.2)
        text = resp.get("choices", [])[0].get("text", "")
    else:
        text = "AI Czar is not available (local model missing). Ensure you have a licensed ggml model and set LLAMA_MODEL_PATH."
    return jsonify({"reply": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
