
import os
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# STEP 1: Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# STEP 2: Read CSV dataset
BASE_DIR = Path(__file__).resolve().parent

DATASET_PATH = BASE_DIR / "sample_data" / "sales_data.csv"

df = pd.read_csv(DATASET_PATH)

print("Dataset loaded successfully!")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))

# STEP 3: Prepare dataset information
dataset_info = df.to_string(index=False)

# STEP 4: Connect to Gemini
client = genai.Client(
    api_key=api_key,
    http_options={"timeout": 60000}
)

print("\nAI Data Analyst is ready!")

# STEP 5: Ask user a question
question = input("\nAsk a question about your sales data: ")

# STEP 6: Prepare AI prompt
prompt = f"""
You are an expert Data Analyst.

Analyze the following sales dataset:

{dataset_info}

Answer the user's question using only the
information available in this dataset.

If information is unavailable, clearly say so.
Explain your answer in simple language.

User Question: {question}
"""

# STEP 7: Generate AI answer
try:
    print("\nGemini is analyzing your data...")

    response = client.interactions.create(
        model="gemini-4-hydrogen",
        input=prompt
    )

    print("\n========== AI ANALYST ANSWER ==========")
    print(response.output_text)
    print("=======================================")

except Exception as e:
    print("\nSomething went wrong:")
    print(type(e).__name__, e)
