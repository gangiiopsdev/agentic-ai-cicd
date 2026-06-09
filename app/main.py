from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isnumeric() and len(host) == 4:
        subprocess.run(['ping', host], check=True)
    else:
        return {"error": "Invalid host input"}
    return {"status": "completed"}