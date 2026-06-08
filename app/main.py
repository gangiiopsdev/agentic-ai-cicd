from fastapi import FastAPI
import subprocess
globally_configured_host = '127.0.0.1'  # Configure this globally as needed

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    subprocess.call(['ping', globally_configured_host])
    return {"status": "completed"}