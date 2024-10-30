import json
import requests
import urllib3
import uuid
import os
from dotenv import dotenv_values
from typing import Any


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class GigaChatLLM():
    def __init__(self) -> None:
        super().__init__()

        if os.getenv('AUTH_DATA') is None:
            self.auth_data = str(dotenv_values(".env")['AUTH_DATA'])
        else:
            self.auth_data = str(os.getenv('AUTH_DATA'))

        self.message_history = []

    def get_access_token(self):
        url = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'
        headers = {
            'Authorization': f'Bearer {self.auth_data}',
            'RqUID': f'{uuid.uuid4()}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'scope': 'GIGACHAT_API_PERS'
        }

        response = requests.post(url, headers=headers, data=data, verify=False)

        return response.json()['access_token']

    def ensure_fit(self, max_tokens = 2048):
        total_tokens = sum(message['tokens'] for message in self.message_history)
        while total_tokens > max_tokens:
            removed_message = self.message_history.pop(0)
            total_tokens -= removed_message['tokens']

    def update_message_history(self, text, response_json):
        self.message_history.append({
            "role": "user",
            "content": text,
            "tokens": response_json['usage']['prompt_tokens']
        })

        self.message_history.append({
            "role": "assistant",
            "content": response_json['choices'][0]['message']['content'],
            "tokens": response_json['usage']['completion_tokens']
        })
    

    def generate(self, text, use_history = False):
        url = 'https://gigachat.devices.sberbank.ru/api/v1/chat/completions'

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.get_access_token()}',
        }

        self.ensure_fit()
        
        data = {
            "model": "GigaChat:latest",
            "messages": [
            ] + self.message_history + [
                {
                "role": "user",
                "content": text
                }
            ] if use_history else [
                {
                "role": "user",
                "content": text
                }
            ],
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, data = json.dumps(data), verify=False)

        self.update_message_history(text, response.json())

        return response.json()['choices'][0]['message']['content']
    
    def response(self, request: str) -> Any:
        return self.generate(request)
