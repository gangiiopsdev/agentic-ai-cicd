from fastapi import FastAPI
import subprocess

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.'))

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in ('-', '.') for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    sanitized_host = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, timeout=5)
    if sanitized_host.returncode == 0:
        return {'status': 'completed', 'output': sanitized_host.stdout}
    else:
        return {'status': 'failed', 'error': sanitized_host.stderr}