from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c if c.isalnum() or c in '._-' else '_' for c in host)

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    host = escape_host(host)
    return safe_ping(host)