import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(content: str) -> str:
    print("openai.api_key: ", openai.api_key)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional news summarizer."},
                {"role": "user", "content": f"Summarize the following article:\n\n{content}"}
            ],
            max_tokens=300,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI Error:", e)
        return ""
