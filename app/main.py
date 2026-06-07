from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        raise ValueError('Invalid hostname')
    cmd = ['ping', '-c', '1', host]
    subprocess.run(cmd, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping_secure(host: str):
    return ping(host)