from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    # Sanitize input to prevent command injection
    sanitized_host = subprocess.list2cmdline(args[1:])
    subprocess.call(['ping'] + [sanitized_host])
    return {"status": "completed"}