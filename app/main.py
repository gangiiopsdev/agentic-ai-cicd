from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        response = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': response.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex to check for allowed hosts
    return True