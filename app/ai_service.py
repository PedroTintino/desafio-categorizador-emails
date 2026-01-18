import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_email(content: str):
    prompt = f"""
Você é um assistente que classifica emails.

Classifique o email abaixo como:
- Produtivo
- Improdutivo

Depois, gere uma resposta curta e educada adequada à categoria.

Email:
\"\"\"{content}\"\"\"

Retorne no formato:
Categoria: <Produtivo|Improdutivo>
Resposta: <texto>
"""
    
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}  
    ],
    temperature=0.2
)


    text = response.choices[0].message.content

    category = "Produtivo" if "Produtivo" in text else "Improdutivo"
    suggested_response = text.split("Resposta:")[-1].strip()

    return category, suggested_response