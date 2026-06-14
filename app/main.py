from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input to prevent shell injection
    valid_hosts = ['example.com', 'localhost']  # Example list of allowed hosts
    if host in valid_hosts:
        args = ['ping', host]
        subprocess.run(args, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}