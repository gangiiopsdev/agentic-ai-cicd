from fastapi import FastAPI
import subprocess
global ping_sanitize_func
ping_sanitize_func = lambda x: ''.join(e for e in x if e.isalnum() or e in ['.', '-', '_'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = ping_sanitize_func(host)
    try:
        subprocess.call(['ping', sanitized_host], shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}