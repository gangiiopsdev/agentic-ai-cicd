from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using parameterized command
    if host and all(c.isalnum() or c in ('.', '-', '_') for c in host):
        subprocess.call(['ping', host])
    else:
        return {"status": "invalid host", "message": "Invalid hostname provided"}
    return {"status": "completed"}