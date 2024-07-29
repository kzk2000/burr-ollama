# Chatbot leveraging Ollama and Burr

***WORK IN PROGRESS***

### One-time setup
* Install Nvidia toolkit on Ubuntu https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
* Configure GPU usage for docker
    ```bash
    sudo nvidia-ctk runtime configure --runtime=docker
    sudo systemctl restart docker
    ```

### Start the containers
```docker-compose up -d```

### Download models within the Ollama container (only required to do once)
```bash
docker exec -it ollama bash
ollama pull llama3.1
ollama pull mxbai-embed-large
```

### Open the Streamlit app
Go to http://localhost:8501/

### References 
* [How to run Ollama locally on GPU with Docker](https://medium.com/@srpillai/how-to-run-ollama-locally-on-gpu-with-docker-a1ebabe451e0)
* [Embedding models](https://ollama.com/blog/embedding-models)