from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host in ['example.com', '127.0.0.1']:  # Example validation
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"status": "invalid host"}