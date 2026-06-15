from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))[:100]

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'error', 'output': 'Invalid host'}
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}