from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.strip():
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}