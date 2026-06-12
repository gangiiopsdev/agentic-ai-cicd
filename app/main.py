from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it is a valid hostname or IP address
    if not host.strip() or not (host.strip().isdigit() or '-' in host):
        return {"status": "invalid input", "message": "Invalid hostname or IP address"}
    subprocess.call(['ping', '-c 4', host])
    return {"status": "completed"}