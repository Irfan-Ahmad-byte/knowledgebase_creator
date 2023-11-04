from langchain.callbacks.base import BaseCallbackHandler

import os


class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)


def save_file(file):
    folder = 'tmp'
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    file_path = f'./{folder}/{file.name}'
    with open(file_path, 'wb') as f:
        f.write(file.getvalue())
    return file_path