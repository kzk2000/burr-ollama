from typing import Generator, List

import ollama
import streamlit as st


def ollama_generator(model_name: str, messages: List) -> Generator:
    stream = ollama.chat(model=model_name, messages=messages, stream=True)
    for chunk in stream:
        yield chunk['message']['content']


st.title("Burr-Ollama with Streamlit")

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "llama3.1:latest"

if "messages" not in st.session_state:
    st.session_state.messages = []

st.session_state.selected_model = st.selectbox(
    "Please select the model:",
    [model["name"] for model in ollama.list()["models"] if model['name'].startswith('llama')])

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you?"):
    # add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # display bot message response container
    with st.chat_message("assistant"):
        response = st.write_stream(ollama_generator(st.session_state.selected_model, st.session_state.messages))
        st.session_state.messages.append({"role": "assistant", "content": response})

# st.header("hamilton")
#
# from hamilton import driver, base
# import my_functions
#
# dr = (
#     driver.Builder()
#     .with_modules(my_functions)
#     .with_adapters(base.PandasDataFrameResult())
#     .build()
# )
#
# output_columns = [
#     "acquisition_cost_rolling_mean_7"
# ]
#
# result = dr.execute(output_columns)
# st.write(result)
#
#
# cache_file = './hamilton_test.png'
# dr.visualize_execution(output_columns, cache_file, {'format': 'png'})
#
#
# st.image(cache_file)
