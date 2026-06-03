from fastapi import FastAPI
import subprocess
import shlex

class SanitizedInput:
    def __init__(self, allowed_chars):
        self.allowed_chars = allowed_chars

    def __getitem__(self, item):
        return ''.join(char for char in item if char in self.allowed_chars)

allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'  # Adjust as needed
sanitize_host = SanitizedInput(allowed_chars)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host[host]
    # Secure implementation
    subprocess.run(['ping', sanitized_host], check=True, text=True)
    return {'status': 'completed'}