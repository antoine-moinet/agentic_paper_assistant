from retriever import retrieve_chunks
from prompts import build_prompt
from openai import OpenAI

"""
client = OpenAI(api_key="sk-...")

def answer_query(query):
    context = retrieve_chunks(query)
    prompt = build_prompt(query, context)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
"""

def answer_query(query):
    context = retrieve_chunks(query)
    prompt = build_prompt(query, context)
    
    return prompt