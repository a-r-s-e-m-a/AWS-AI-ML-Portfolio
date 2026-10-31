# Week 1: Student Marks Data Processing

## Project Overview

This project is a small Python data-processing application that loads student marks from a CSV file, cleans invalid records, and performs basic statistical analysis using NumPy.

The project demonstrates how raw data can be organized, cleaned, and processed to produce meaningful results.

## Objectives

- Load student records from a CSV file.
- Clean student names and validate marks.
- Remove records containing missing or invalid data.
- Use NumPy to perform numerical calculations.
- Generate a summary report of student performance.

## Technologies Used

- Python
- NumPy
- CSV
- Jupyter Notebook
- Google Colab

## Project Files

| File | Description |
|---|---|
| `main.py` | Main Python application |
| `students.csv` | Sample student marks dataset |
| `requirements.txt` | Required Python library |
| `Student_Marks_Data_Processing.ipynb` | Interactive Google Colab notebook |

### Google Colab Notebook

[Open Student Marks Data Processing in Google Colab](https://colab.research.google.com/drive/1DEjyj2uRUr_jWohekYm082I1uHV5WT77?usp=sharing)

The notebook contains the complete implementation, including data loading, cleaning, NumPy processing, and the final report.

## Data Cleaning

The application applies the following rules:

- Removes unnecessary spaces from student names.
- Rejects records with missing marks.
- Rejects marks outside the valid range of 0–100.
- Keeps only valid student records.

## Analysis and Results

The application uses NumPy to calculate:

- Average mark
- Highest mark
- Lowest mark
- Number of students who passed
- Number of students who failed

### Sample Results

| Measurement | Result |
|---|---:|
| Original records | 7 |
| Valid records | 5 |
| Removed records | 2 |
| Average mark | 70.6 |
| Highest mark | 91 |
| Lowest mark | 45 |
| Passed | 4 |
| Failed | 1 |

## How to Run

1. Install Python.
2. Install the required library:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

Alternatively, open the `.ipynb` notebook in Google Colab and execute the cells in order.

## Learning Outcomes

Through this project, I practiced working with CSV datasets, writing Python functions, handling invalid data, using NumPy for numerical analysis, and running Python projects in different development environments.
