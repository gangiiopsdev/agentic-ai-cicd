from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to escape shell metacharacters
    safe_host = subprocess.shlex_quote(host)
    subprocess.run(['ping', safe_host], check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = subprocess.shlex_quote(host)
    subprocess.run(['ping', safe_host], check=True)
    return {'status': 'completed'}