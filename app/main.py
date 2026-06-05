from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using shlex.quote to sanitize input
    subprocess.run(['ping', '-c', shlex.quote(host)], check=True)
    return {'status': 'completed'}