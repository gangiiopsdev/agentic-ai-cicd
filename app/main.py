from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    safe_host = host.replace(';', '').replace('&', '')
    subprocess.run(['ping', safe_host], check=True)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}