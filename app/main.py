from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    if not all(c in string.ascii_letters + '.' for c in host):  # Validate input to be alphanumeric or '.', which are safe characters for ping targets
        return {'status': 'failed', 'error': 'Invalid host name'}
    return ping(host)