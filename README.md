# ISP - Group Project (Python)

A Python project for fetching and working with UCI Machine Learning Repository datasets.

## Overview

This project demonstrates how to fetch datasets from the UCI Machine Learning Repository using the `ucimlrepo` library. Currently configured to fetch the Spambase dataset (ID 94).

## Requirements

- Python 3.12+
- Virtual environment (`.venv`)

## Installation

1. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install required packages:
```bash
pip install ucimlrepo pandas
```

## Usage

Run the main script:
```bash
python main.py
```

Or using the virtual environment directly:
```bash
.venv/bin/python main.py
```

## Output

The script fetches the Spambase dataset and displays:
- Total number of rows and columns
- First 5 rows of the dataset

Example output:
```
Fetching data from UCI...
Data loaded successfully!
Total rows: 4601
Total columns: 57

First 5 rows of data:
   word_freq_make  ...  capital_run_length_total
0            0.00  ...                       278
1            0.21  ...                      1028
...
```

## Dataset

The Spambase dataset contains 4601 email samples with 57 features representing word frequencies and other characteristics, used for spam detection classification.

## Project Structure

```
python-sayang/
├── main.py          # Main script to fetch and display UCI data
├── README.md        # Project documentation
└── .venv/           # Virtual environment
```

