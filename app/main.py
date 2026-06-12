from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return {'status': 'completed'}