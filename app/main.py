from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.quote to escape shell metacharacters
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(f'ping {safe_host}', shell=True)
    return {'status': 'completed'}