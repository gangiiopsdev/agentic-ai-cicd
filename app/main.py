from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Safe implementation using shlex.quote to escape arguments
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(shlex.quote(host))
    return {'status': 'completed'}