import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def analyze_logs(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Log file '{file_path}' not found.")
        return

    with open(file_path, "r") as f:
        log_data = f.read()

    prompt = f"""
    You are an expert system administrator and security analyst. 
    Analyze the following system logs for critical errors, performance bottlenecks, or security anomalies.
    
    Provide a response in the following structured format:
    1. Summary of Issues Found
    2. Severity Level (Low/Medium/High/Critical)
    3. Actionable Resolution Steps

    Logs:
    {log_data}
    """

    print("Analyzing logs with open-weight Gemma model...\n")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    print("=== ANALYSIS REPORT ===")
    print(response.text)

if __name__ == "__main__":
    analyze_logs("server.log")