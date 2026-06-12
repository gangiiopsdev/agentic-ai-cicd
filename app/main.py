from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.quote
    import shlex
    subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), check=True)
    return {'status': 'completed'}