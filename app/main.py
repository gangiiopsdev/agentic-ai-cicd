from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    return {"status": ping(host)}