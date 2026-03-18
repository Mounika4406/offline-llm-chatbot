Offline Customer Support Chatbot using Ollama and Llama 3.2
Project Overview

This project implements an offline customer support chatbot for a fictional e-commerce store called Chic Boutique.
The chatbot uses a local Large Language Model (LLM) powered by Ollama and Meta's Llama 3.2 (3B) model.

The main goal of the project is to demonstrate how businesses can build AI-powered tools while ensuring data privacy by running models entirely on local hardware instead of sending customer data to external APIs.

The chatbot processes customer queries and generates responses using two prompt engineering strategies:

Zero-Shot Prompting

One-Shot Prompting

The results from both methods are evaluated and compared.

Key Features

Runs completely offline

Uses Ollama local LLM server

Implements Llama 3.2 (3B) model

Demonstrates Prompt Engineering

Compares Zero-Shot vs One-Shot prompting

Logs chatbot responses for manual evaluation

Project Structure
offline-chatbot
│
├── chatbot.py                # Main Python script to interact with Ollama API
├── README.md                 # Project documentation
├── setup.md                  # Setup and installation instructions
├── report.md                 # Project analysis and evaluation report
│
├── prompts
│   ├── zero_shot_template.txt
│   └── one_shot_template.txt
│
├── eval
│   └── results.md            # Evaluation results and scoring
Technologies Used

Python

Ollama

Llama 3.2 (3B)

Requests Library

Ubuntu Dialogue Corpus Dataset

How the Chatbot Works

The Python script reads a list of customer queries.

Each query is inserted into two prompt templates:

Zero-Shot Template

One-Shot Template

The prompts are sent to the Ollama API running locally.

The Llama 3.2 model generates responses.

Responses are logged into eval/results.md.

The results are manually evaluated based on:

Relevance

Coherence

Helpfulness

Prompt Engineering Methods
Zero-Shot Prompting

The model receives only instructions and the customer query without any example.

One-Shot Prompting

The prompt includes one example query and response to guide the model in generating better answers.

Evaluation Criteria

The chatbot responses are evaluated manually based on three metrics:

Metric	Description
Relevance	How well the response answers the customer question
Coherence	Whether the response is clear and grammatically correct
Helpfulness	Whether the response provides useful information

Each response is scored from 1 (Poor) to 5 (Excellent).

Running the Chatbot

Make sure the Ollama server is running and the model is installed.

Run the chatbot using:

python chatbot.py

The results will be saved in:

eval/results.md
Learning Outcomes

Through this project we learn:

How to run LLMs locally

How to interact with models using REST APIs

Fundamentals of prompt engineering

How to evaluate LLM generated responses

Benefits of privacy-preserving AI systems

Conclusion

This project demonstrates that local LLM deployment using Ollama is a viable solution for building privacy-friendly AI applications. While smaller models like Llama 3.2 (3B) may not be as powerful as larger cloud models, they still provide useful responses and can be used for many real-world applications such as customer support automation.