from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if host in ['localhost', '127.0.0.1']:  # Allow only trusted hosts
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"status": "Invalid host", "error": "Only localhost and 127.0.0.1 are allowed"}