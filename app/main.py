from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation to ensure host does not contain harmful characters
    if any(char in host for char in [';', '&', '|', '&&', '||']):
        raise ValueError('Invalid host input')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}