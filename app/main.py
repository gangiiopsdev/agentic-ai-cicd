from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with full path and input validation
    if host.isalnum():
        subprocess.run(['/bin/ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    # Secure implementation with full path and input validation
    if host.isalnum():
        subprocess.run(['/bin/ping', host], check=True)