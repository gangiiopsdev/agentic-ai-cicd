from fastapi import FastAPI
import subprocess

def run_ping(host):
    # Safer implementation using shlex.quote to escape host input
    safe_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', safe_host], check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    run_ping(host)
    return {'status': 'completed'}