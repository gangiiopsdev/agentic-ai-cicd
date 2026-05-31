from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using a whitelist for allowed hosts or validate the host input
    if host not in ['example.com', 'test.com']:
        return {"error": "Invalid host"}
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    # Secure implementation using a whitelist for allowed hosts or validate the host input
    if host not in ['example.com', 'test.com']:
        return {"error": "Invalid host"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}