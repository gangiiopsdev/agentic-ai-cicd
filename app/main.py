from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    if host not in allowed_hosts:
        return {"error": "Invalid host"}, 403
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}