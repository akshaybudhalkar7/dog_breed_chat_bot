# Dog Breed Chat Bot

This repository contains a Dog Breed Chat Bot application built using Python and Natural Language Processing (NLP) techniques. The bot is designed to identify and provide information about different dog breeds based on user input.

## Features

- **Breed Identification:** The bot can identify various dog breeds from user descriptions.
- **Breed Information:** Provides detailed information about the identified breed, including characteristics, temperament, and more.
- **Interactive Chat Interface:** Users can interact with the bot conversationally.

## Installation

To set up the bot locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/akshaybudhalkar7/dog_breed_chat_bot.git
   cd dog_breed_chat_bot
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a main directory**
   inside that create other directories
   
4. **Source Data:**
   Create a data directory in the main folder
   "data/"

5. **Vectorstore**
Create a vectorstores directory and inside that create db_faiss directory 
"vectorstores/db_faiss"

6. **Run the application:**
   ```bash
   python ingest.py
   chainlit run model.py
   ```

7. **Download the LLM Model:**
   Download the LLM model from Hugging Face using the link below:
   - [Llama-2-7B-Chat GGML Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin)
   - Place the bin file in main directory

## Project Structure

- **`ingest.py`**: This Python script creates a vector store from the `Dog-breed-book-low-resolution.pdf`.
- **`model.py`**: This script is used for running the chat bot.
- **`data/`**: The directory contains `dog-breed-book-low-resolution.pdf` that is used by `ingest.py` to create a vector store.
- **`vectorstores/db_faiss/`**: This directory contains `index.faiss` and `index.pkl`.
- **`llama-2-7b-chat.ggmlv3.q8_0.bin`**: This is the LLM model used for the chat bot.
- **`requirements.txt`**: A list of Python packages required to run the project.
- **`chainlit.md`**: Chainlit lib details.

  ## Please refer below image for files structure
  ![image](https://github.com/user-attachments/assets/248533fa-93a0-40ca-8856-1031ddf4206c)


---



You can update the README based on any further details or adjustments you might need!
