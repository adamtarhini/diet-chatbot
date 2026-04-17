# Diet Chatbot

This is a simple AI chatbot I built to answer questions about diet and nutrition.
It uses a fine-tuned FLAN-T5 model and a custom dataset of Q&A related to healthy eating.

I mainly built this project to learn more about NLP, transformers, and how chatbots actually work.

---

## What it does

* Answers basic questions about diet and nutrition
* Uses a trained model instead of hardcoded responses
* Has a simple web interface (Flask)

---

## How to run it

First install the requirements:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python app.py
```

Open your browser and try asking questions.

---

## About the model

The chatbot is based on FLAN-T5 and trained on a dataset of around 500+ nutrition Q&A pairs.

The trained model is not included here because it's too large for GitHub.

---

## Files

* `app.py` → main chatbot code
* `templates/` → frontend
* `diet_qa_combined.json` → dataset
* `ChatBot.ipynb` → experiments and testing

---

## Notes

The answers are not perfect yet and sometimes can be repetitive or generic.
This is something I plan to improve by training on better data.

---

## Why I made this

I wanted to try building something practical with AI instead of just following tutorials.
This project helped me understand how fine-tuning works and how to connect a model to a simple app.

---

## Future improvements

* Improve dataset quality
* Make answers more natural
* Add better UI
* Deploy it online

---

## Author

Adam Tarhini
