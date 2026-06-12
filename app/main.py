from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent shell injection
    safe_host = shlex.quote(host)
    args = ['ping', safe_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}