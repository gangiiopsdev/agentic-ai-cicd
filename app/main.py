from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Enhanced validation and sanitization
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or '.' not in host:
        return {"status": "invalid_host"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}