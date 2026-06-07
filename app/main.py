from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output to avoid shell=True and validate input
    if host in ['localhost', '127.0.0.1']:  # Example validation
        subprocess.check_output(['ping', '-c', '1', host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}