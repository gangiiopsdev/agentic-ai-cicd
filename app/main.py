from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if host.isalnum():
        subprocess.call(['ping', host])
    else:
        return {"error": "Invalid input"}
    return {"status": "completed"}