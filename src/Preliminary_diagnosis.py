import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def prel_diagnosis(Symptoms: list[str]) -> str:
    prompt = f"The patient has these symptoms: {', '.join(Symptoms)}. Suggest a preliminary diagnosis based on these symptoms."
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful and professional medical expert. Provide a preliminary diagnosis based on the symptoms provided."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
        
    )
    return response.choices[0].message.content.strip()
    
    
output= prel_diagnosis(["fever", "cough"])
print(output)
    