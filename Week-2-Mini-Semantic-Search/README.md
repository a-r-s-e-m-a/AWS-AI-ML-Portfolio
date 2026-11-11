# Week 2: Mini Semantic Search

## Project Overview

This project implements a Mini Semantic Search system using Python. It searches frequently asked questions (FAQs) based on their meaning rather than relying only on exact keyword matches.

## Technologies Used

- Python
- Pandas
- Sentence Transformers
- ChromaDB
- NumPy

## Project Features

- Load FAQ data from a CSV file using Pandas.
- Clean text by converting it to lowercase and removing unnecessary spaces.
- Split text into smaller chunks.
- Generate text embeddings using the `all-MiniLM-L6-v2` model.
- Store embeddings in ChromaDB.
- Search for FAQs based on the meaning of a query.
- Return the top 3 matching questions and answers.

## Project Files

- `main.py` – Python source code.
- `Mini_Semantic_Search.ipynb` – Google Colab notebook containing the code, explanations, and outputs.
- `faqs.csv` – FAQ questions and answers.
- `requirements.txt` – Required Python libraries.
- `README.md` – Project documentation.

## Example Search

**Search Query:**

How can computers learn from information?

**Top 3 Matching Results:**

1. What is Machine Learning?
2. What is Artificial Intelligence?
3. What is Deep Learning?

## How to Run

1. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

2. Make sure `faqs.csv` is in the project folder.

3. Run the program:

   ```bash
   python main.py
   ```

## Learning Outcomes

Through this project, I practiced working with text data, embeddings, vector databases, and semantic search techniques.
