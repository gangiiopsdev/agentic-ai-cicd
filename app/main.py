from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host], shell=False)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using shlex.quote to escape command arguments
    safe_ping(host)
    return {'status': 'completed'}