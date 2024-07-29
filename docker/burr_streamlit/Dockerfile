FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    curl \
    git \
    graphviz \
    tree \
    && rm -rf /var/lib/apt/lists/*

# add Python packages
COPY requirements.txt /requirements.txt
RUN pip3 install -r ./requirements.txt

WORKDIR /app
EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py"]