from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    # Add custom sanitization logic here if necessary
    return input_str

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(shlex.split(f'ping {shlex.quote(sanitized_host)}'), check=True)
    return {'status': 'completed'}