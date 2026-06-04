from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize host input
    if not all(char.isalnum() or char in '-.' for char in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)