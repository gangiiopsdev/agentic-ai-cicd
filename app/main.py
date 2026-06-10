from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host in ['localhost', '127.0.0.1']:  # Allow only trusted hosts
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        raise ValueError("Invalid host")