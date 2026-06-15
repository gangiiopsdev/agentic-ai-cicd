from fastapi import FastAPI
import subprocess
from urllib.parse import quote

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in '-._~:/?#@[\]^`{|}+')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', quote(sanitized_host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}