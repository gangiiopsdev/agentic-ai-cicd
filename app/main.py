from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.quote to safely escape the host input
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}