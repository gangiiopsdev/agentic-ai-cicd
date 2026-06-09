from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with full path and input validation
    if 'localhost' in host or '127.0.0.1' in host:
        subprocess.call(['/bin/ping', host])
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}