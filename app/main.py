from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.startswith('-') or '&&' in host or ';' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    return safe_ping(host)