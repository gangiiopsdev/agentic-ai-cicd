from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using list for args and shell=False to avoid shell injection risks
    subprocess.run(['ping', host], check=True, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if '@' not in host and ':' not in host:
        safe_ping(host)
    else:
        raise ValueError("Invalid host parameter")
    return {"status": "completed"}