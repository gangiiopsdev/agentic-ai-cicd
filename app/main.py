from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize the input
    if any(char in host for char in [';', '&', '|', '`']):
        raise ValueError('Invalid characters in host name')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)}