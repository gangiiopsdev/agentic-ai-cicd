from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}