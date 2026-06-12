from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Ensuring the command is safe and not prone to injection attacks
    if not any(char in host for char in [';', '|', '&', '`']):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Unsafe input detected')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}