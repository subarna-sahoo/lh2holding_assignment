from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(content: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional news editor."
                },
                {
                "role": "user",
                "content": (
                    "Summarize the following news article in exactly 4 concise sentences. "
                    "Fix any grammar or sentence structure issues, and remove redundancy. "
                    "Focus on the most important facts: who, what, where, when, and why. "
                    "Do not include phrases like 'the article says' or 'more info can be found'. "
                    "Format your response as plain text with each sentence on a new line.\n\n"
                    f"{content}"
                )
                }
            ],
            max_tokens=400,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI Error:", e)
        return ""
