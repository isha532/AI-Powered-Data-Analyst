
import os
from dotenv import load_dotenv
from google import genai


def ask_gemini(df, question):
    """
    Analyze uploaded dataset and answer user's question using Gemini.
    """

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API key not found in .env file")

    if df is None or df.empty:
        raise ValueError("Dataset is empty. Please upload valid data.")

    if not question or not question.strip():
        raise ValueError("Please enter a question.")

    client = genai.Client(
        api_key=api_key,
        http_options={"timeout": 60000}
    )

    dataset_info = df.head(100).to_string(index=False)

    prompt = f"""
    You are an expert Data Analyst.

    Analyze the following dataset:

    {dataset_info}

    Answer the user's question using only the information
    available in this dataset.

    If information is unavailable, clearly say so.
    Explain your answer in simple language.

    User Question: {question}
    """

    response = client.interactions.create(
        model="gemini-4-hydrogen",
        input=prompt
    )

    return response.output_text
