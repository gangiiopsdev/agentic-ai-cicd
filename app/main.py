from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    if not all(char.isalnum() or char in ' .-' for char in host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}