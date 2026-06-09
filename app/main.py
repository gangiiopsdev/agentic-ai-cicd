from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}