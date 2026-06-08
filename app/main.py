from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safer implementation using subprocess.run and shlex.split to avoid shell injection
    import shlex
    subprocess.run(['ping', *shlex.split(host)], check=True, text=True)
    return {'status': 'completed'}