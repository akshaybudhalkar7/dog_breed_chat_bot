Dog Breed Chat Bot
This repository contains a Dog Breed Chat Bot application built using Python and Natural Language Processing (NLP) techniques. The bot is designed to identify and provide information about different dog breeds based on user input.

Features
Breed Identification: The bot can identify various dog breeds from user descriptions.
Breed Information: Provides detailed information about the identified breed, including characteristics, temperament, and more.
Interactive Chat Interface: Users can interact with the bot conversationally.

Installation
To set up the bot locally, follow these steps:

Clone the repository:
git clone https://github.com/akshaybudhalkar7/dog_breed_chat_bot.git
cd dog_breed_chat_bot

Install the required dependencies:
pip install -r requirements.txt

Run the application:
python ingest.py
chainlit run model.py

Download the LLM Model from hugging face using below link
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin

Project Structure
ingest.py: This Python script creates a vector store from the Dog-breed-book-low-resolution.pdf.
models.py: This script.
data/: The directory contains a dog-breed-book-low-resolution.pdf that is used by ingest.py to create a vector store.
vectorstores/db_faiss/: This directory contains index.faiss and index.pkl
llama-2-7b-chat.ggmlv3.q8_0.bin: This is the LLM model which we are using for our chat bot.
requirements.txt: A list of Python packages required to run the project
