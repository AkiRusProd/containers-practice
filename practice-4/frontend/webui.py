import gradio as gr
import random
import time
import requests


def memory_response(message, collection_name, n_results = 3, memory_access_threshold = 1.5):
    url = "http://llm-rag:9000/memory_response" #localhost
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json={"prompt": message, "collection_name": collection_name, "n_results": n_results, "memory_access_threshold": memory_access_threshold}, headers=headers)

    if response.status_code == 200:
        response = response.text[1:-1].replace("\\n\\n","\n\n").replace("\\n","\n")
    else:
        response = f"Error: {response.status_code}"

    return response

def response(message):
    url = "http://llm-rag:9000/response" #localhost
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json={"prompt": message}, headers=headers)

    if response.status_code == 200:
        response = response.text[1:-1].replace("\\n\\n","\n\n").replace("\\n","\n")
    else:
        response = f"Error: {response.status_code}"

    return response

def respond(message, collection_choice, n_results, memory_access_threshold, chat_history):
    bot_message = memory_response(message, collection_choice, n_results, memory_access_threshold)
    # bot_message = response(message)
    chat_history.append((message, bot_message))
    # time.sleep(2)
    return "", chat_history

def choose_collection(collection_choice):
    return collection_choice

collections = [
    "default",
    "medicine",
    "food",
    "animals",
    "fashion",
]

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1):
            # First variant
            collection_choice = gr.Textbox(label="Collection", value=collections[0])
            buttons = [gr.Button(collection) for collection in collections]

            # Second variant
            # collections_dropdown = gr.Dropdown(collections, label="Collection")

        with gr.Column(scale=3):
            chatbot = gr.Chatbot()
            msg = gr.Textbox(placeholder="Type a message...")

            with gr.Row():
                clear_btn = gr.ClearButton([msg, chatbot])
                submit_btn = gr.Button(value="Send")
                n_results_slider = gr.Slider(minimum=1, maximum=10, value=3, step=1, label="N results")
                memory_access_threshold_slider = gr.Slider(minimum=0.0, maximum=2.0, value=1.5, step=0.1, label="Memory access threshold")

            msg.submit(respond, [msg, collection_choice, n_results_slider, memory_access_threshold_slider, chatbot], [msg, chatbot])

    submit_btn.click(respond, [msg, collection_choice, n_results_slider, memory_access_threshold_slider, chatbot], [msg, chatbot])

    for button in buttons:
        button.click(choose_collection, [button], [collection_choice])

if __name__ == "__main__":
    demo.launch(debug = True, server_port = 7860, share=False, server_name="0.0.0.0")