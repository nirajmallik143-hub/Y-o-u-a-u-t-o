import os
from google import genai

def generate_script(video_type="short"):
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    if video_type == "short":
        prompt = "Write a 50-word ultra-engaging, viral YouTube Short script about a dark psychology trick or mind-blowing historical fact. Start with an immediate hook."
    else:
        prompt = "Write a 500-word captivating Reddit-style story or mystery script for a long-form YouTube video targeted at a US audience. Include an intro, rising tension, and a cliffhanger/twist ending."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text

if __name__ == "__main__":
    print("Script Generated successfully.")
