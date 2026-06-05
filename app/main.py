from fastapi import FastAPI
import subprocess
import shlex

def secure_ping(host: str):
    escaped_host = shlex.quote(host)
    subprocess.run(['ping', escaped_host], check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}