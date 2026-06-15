from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host name"}, 400
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}