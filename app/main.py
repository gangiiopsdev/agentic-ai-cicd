from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if all(char.isalnum() or char in ['-', '.'] for char in host):  # Simple validation of the host input
        return ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host name'}