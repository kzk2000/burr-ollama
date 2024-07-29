import ollama

model = 'llama3.1'

response = ollama.chat(model=model, messages=[
    {
        'role': 'user',
        'content': 'What is a LLM?',
    },
])
print(response['message']['content'])
