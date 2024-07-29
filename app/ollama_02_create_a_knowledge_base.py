"""
Example snippets from https://ollama.com/blog/embedding-models
"""
import ollama
import chromadb

model = 'llama3.1'
embedding_model = "mxbai-embed-large"

# create a knowledge base, here each row is 1 document
documents = [
    "Llamas are members of the camelid family meaning they're pretty closely related to vicuñas and camels",
    "Llamas were first domesticated and used as pack animals 4,000 to 5,000 years ago in the Peruvian highlands",
    "Llamas can grow as much as 6 feet tall though the average llama between 5 feet 6 inches and 5 feet 9 inches tall",
    "Llamas weigh between 280 and 450 pounds and can carry 25 to 30 percent of their body weight",
    "Llamas are vegetarians and have very efficient digestive systems",
    "Llamas live to be about 20 years old, though some only live for 15 years and others live to be 30 years old",
]

# upload to ChromaDB
client = chromadb.Client()
if client.count_collections() > 0:
    client.delete_collection("docs")

collection = client.create_collection(name="docs", get_or_create=True)

# store each document in a vector embedding database
for i, d in enumerate(documents):
    response = ollama.embeddings(model=embedding_model, prompt=d)
    embedding = response["embedding"]
    collection.upsert(
        ids=[str(i)],
        embeddings=[embedding],
        documents=[d]
    )

# create an example prompt
#prompt = "What animals are llamas related to?"
prompt = "How old does a Llama get?"

# generate an embedding for the prompt and retrieve the most relevant doc
response = ollama.embeddings(
    prompt=prompt,
    model=embedding_model,
)
results = collection.query(
    query_embeddings=[response["embedding"]],
    n_results=3,
)
data = results['documents']

# create the final answer
output = ollama.generate(
    model=model,
    # prompt=f"Using this data: {data}. Respond to this prompt: {prompt}"
    prompt=f"Using this list of input docs: {data}. Follow these instructions: "
           f"1. Respond to this prompt: {prompt}"
           f"2. Provide a confidence score between 0 and 100."
           f"3. Only use information from the input docs."
           f"4. Reference which doc was used.",
)

print(output['response'])
