from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    # Use a whitelist of allowed hosts or sanitize the input
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}