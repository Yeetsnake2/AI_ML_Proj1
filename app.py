import gradio as gr
from rag import upsert_txtpdf
from agent import agent


def handle_upload(files, prev_text):
    return_string = ""
    for file in files:
        file_path = file.name
        upsert_txtpdf(file_path)
        return_string += f"{file_path}\n"
    if prev_text:
        return_string = prev_text + return_string
    return return_string

def run_agent(message, _):
    agent_response = agent.invoke({"messages": [{"role": "user", "content": message}]}, {"configurable": {"thread_id": "1"}})
    return agent_response['messages'][-1].content

def main():
    with gr.Blocks() as demo:
        with gr.Row(scale=2, min_height=600):
            with gr.Column(scale=2):
                gr.ChatInterface(
                fn=run_agent, 
                type="messages"
                )
            with gr.Column():
                b = gr.Textbox(label="Files uploaded:", interactive=False, lines=24)
                u = gr.UploadButton("Upload a file", file_types=["text"], file_count="multiple")
        dummy = gr.State()
        u.upload(fn=lambda files, text: (files, text), inputs=[u, b], outputs=dummy)
        dummy.change(fn=lambda text: handle_upload(text[0], text[1]) if text else gr.skip(), inputs=dummy, outputs=b)

    demo.launch(inbrowser=True, prevent_thread_lock=False)

if __name__ == "__main__":
    main()