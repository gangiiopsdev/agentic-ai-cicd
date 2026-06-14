from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or '&&' in host or ';' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}