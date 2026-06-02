from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Sanitize input to prevent command injection
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    run_ping(host)
    return {'status': 'completed'}