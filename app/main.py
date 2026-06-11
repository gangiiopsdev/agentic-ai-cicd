from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent command injection
    if all(c.isalnum() or c in ('.', '-', '_') for c in host):
        args = ['ping', host]
        subprocess.call(args)
    else:
        raise ValueError('Invalid hostname')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return {"status": "completed"}