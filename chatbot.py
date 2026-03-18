import requests
import json

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_ENDPOINT, json=payload)
    return response.json()["response"].strip()


with open("prompts/zero_shot_template.txt") as f:
    zero_template = f.read()

with open("prompts/one_shot_template.txt") as f:
    one_template = f.read()


queries = [
"How do I track my order?",
"My discount code is not working.",
"How can I change my delivery address?",
"I received the wrong product.",
"How long does shipping take?",
"Can I cancel my order after placing it?",
"How do I return a product?",
"My payment was deducted but order not confirmed.",
"Where can I see my order history?",
"Do you offer free shipping?",
"How can I contact customer support?",
"My package arrived damaged.",
"Can I exchange a product for another size?",
"How do I apply a promo code?",
"I forgot my account password.",
"Can I update my shipping address after ordering?",
"What payment methods do you accept?",
"How do I get a refund?",
"Why is my order delayed?",
"Can I buy gift cards from your store?"
]


with open("eval/results.md", "w") as f:

    f.write("| Query # | Customer Query | Prompt Method | Response | Relevance | Coherence | Helpfulness |\n")
    f.write("|---|---|---|---|---|---|---|\n")

    for i, q in enumerate(queries, 1):

        print("Processing query:", i)

        zero_prompt = zero_template.replace("{query}", q)
        one_prompt = one_template.replace("{query}", q)

        zero_response = query_ollama(zero_prompt)
        one_response = query_ollama(one_prompt)

        f.write(f"| {i} | {q} | Zero-Shot | {zero_response} |  |  |  |\n")
        f.write(f"| {i} | {q} | One-Shot | {one_response} |  |  |  |\n")

print("Done! Check eval/results.md")