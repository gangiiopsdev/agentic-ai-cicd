from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host or not all(c.isalnum() or c in ('-', '.', ':', ';') for c in host):
        return {"status": "invalid_host"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}