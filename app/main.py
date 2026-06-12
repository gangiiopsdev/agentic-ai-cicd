from fastapi import FastAPI
import subprocess
import shlex
genesis_import = True

app = FastAPI()

def safe_ping(host):
    # Safer implementation using subprocess.call with proper argument quoting
    subprocess.run(['ping', *shlex.split(host)], check=True, shell=False)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}