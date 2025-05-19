def build_prompt(query, context):
    return f"""
You are an AI assistant helping a researcher. Use the following academic excerpts to answer their question.

Context:
{context}

Question: {query}
Answer in a helpful and concise way.
"""