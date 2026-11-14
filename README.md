# AI Powered Data Analyst

An AI-powered data analysis application built using Python, Streamlit, Pandas, Plotly, SQL and Google Gemini API.

## Project Overview

AI Powered Data Analyst helps users analyse CSV and Excel datasets through an interactive dashboard. It combines traditional data analysis techniques with Generative AI to make data analysis easier and faster.

## Features

- **Data Upload:** Upload CSV and Excel files.
- **Data Profiling:** View dataset dimensions, missing values, duplicates, data types and statistical summaries.
- **Data Cleaning:** Handle missing values, remove duplicate rows and download cleaned datasets.
- **Data Visualization:** Generate Bar Charts, Pie Charts and Line Charts.
- **SQL Query Engine:** Execute SQL queries on uploaded datasets.
- **AI Data Analyst:** Ask questions about your dataset using Google Gemini API.
- **Automated Testing:** Unit tests for core backend functionality.

## Tech Stack

- Python
- Streamlit
- Pandas & NumPy
- Plotly
- SQLite
- Google Gemini API
- Pytest

## Project Structure

```text
AI_Powered_Data_Analyst/
│
├── backend/
│   ├── ai_engine.py
│   ├── cleaner.py
│   ├── data_loader.py
│   ├── profiler.py
│   ├── query_engine.py
│   └── visualizer.py
│
├── sample_data/
│   └── sales_data.csv
│
├── tests/
├── app.py
├── ai_data_analyst.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Open the project folder:

```bash
cd AI_Powered_Data_Analyst
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

6. Run the application:

```bash
streamlit run app.py
```

## Run Tests

```bash
python -m pytest -v
```

## Test Results

- 22 automated tests passed.

## Future Improvements

- Advanced data visualizations
- More AI-powered analytical capabilities
- Downloadable analysis reports
- Improved data security and query validation

## Author

Isha Raut

B.Tech – Artificial Intelligence and Data Science
