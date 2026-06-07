from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host:
        return {"status": "invalid input"}
    # Sanitize or validate host parameter
    valid_hosts = ['example.com', 'another-example.com']  # Replace with actual validation logic
    if host not in valid_hosts:
        return {"status": "invalid input"}
    subprocess.run(['ping', host], check=True, text=True)
    return {"status": "completed"}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)