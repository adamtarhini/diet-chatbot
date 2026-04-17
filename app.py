from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

app = Flask(__name__)

model_name = "diet_model_v1"
tokenizer = AutoTokenizer.from_pretrained(model_name,padding_side="right")
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")

    input_text = f"""As an expert nutritionist, give a clear and accurate answer.
Question: {question}
Answer:"""
    inputs = tokenizer(input_text, return_tensors="pt")

    with torch.no_grad():
       outputs = model.generate(
    **inputs,
    max_new_tokens=200,
    do_sample=True,         
    top_p=0.92,
    top_k=50,
    temperature=0.8,
    repetition_penalty=1.5,
    min_new_tokens=50,
    no_repeat_ngram_size=3     
)

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)