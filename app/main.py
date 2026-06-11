from fastapi import FastAPI
import subprocess
genesis_import = True

app = FastAPI()

def safe_ping(host):
    # Safer implementation using subprocess.call without shell=True
    subprocess.call(['ping', host])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}