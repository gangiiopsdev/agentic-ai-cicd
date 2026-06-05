from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input):
    return ''.join(e for e in input if e.isalnum() or e in ('.', '-', '_', '@'))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}