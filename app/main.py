from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping_handler(host: str):
    return {'status': 'Pinging', 'host': host}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}