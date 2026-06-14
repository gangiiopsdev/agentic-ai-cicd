from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum() and not '.' in host:
        return {"error": "Invalid host name"}, 400
    subprocess.call(['ping', '-c', '1', host])  # Limit the number of pings to avoid DoS attacks
    return {"status": "completed"}