import os
import json
import sys
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
# Load .env file
load_dotenv()

# ✅ Fail fast if API key not found
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY is missing from .env or environment", file=sys.stderr)
    sys.exit(1)

# ✅ Create OpenAI client with OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={
        "HTTP-Referer": "http://localhost:3000",  # replace with your deployed site if needed
        "X-Title": "ML Code Generator"
    }
)

def generate_ml_code(prompt, headers):
    

    full_prompt = f"""
You are a highly skilled machine learning assistant. Your task is to generate concise and accurate Python code based on the user's request.

Dataset columns: {headers}
Assume the dataset is already loaded into a pandas DataFrame named 'df'.

Instructions:
1. Use only these libraries: pandas, scikit-learn, matplotlib.
2. Always include one of the following:
   - If your output is a plot, save it as: `plt.savefig("output_step_<step>.png")`
   - If your output is a summary or data sample, write it to a file: `with open("output_step_<step>.txt", "w") as f: f.write(...)`
3. Do NOT show plots with `plt.show()`. Only save them.
4. Do not include explanations. Just return code.
5. Make sure the code works directly with the DataFrame 'df'.

User request:
{prompt}

Start your code now:
"""

    try:
        response = client.chat.completions.create(
            model="mistralai/mixtral-8x7b-instruct",
            messages=[
                { "role": "system", "content": "You are a helpful ML coding assistant." },
                { "role": "user", "content": full_prompt }
            ],
            temperature=0.4,
            max_tokens=1000
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python llm_engine.py '<PROMPT>' '<HEADERS_JSON>'", file=sys.stderr)
        sys.exit(1)

    prompt = sys.argv[1]
    headers_json = sys.argv[2]

    try:
        headers = json.loads(headers_json)
        code = generate_ml_code(prompt, headers)
        print(code if code else "No code returned.")
    except json.JSONDecodeError:
        print("Invalid JSON for headers.", file=sys.stderr)
        sys.exit(1)
