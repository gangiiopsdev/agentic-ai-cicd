from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', cmd_quote(host)], check=True)
    return {'status': 'completed'}