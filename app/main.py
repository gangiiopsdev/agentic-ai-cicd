from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if '||' in host or '&' in host or ';' in host:
        return {"status": "failed", "error": "Invalid characters in host name."}
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}