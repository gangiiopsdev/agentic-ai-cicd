from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host not in ['127.0.0.1', '::1']: # Add more allowed hosts as necessary
        return "Invalid host"
    return subprocess.call(['ping', host], shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, int):
        return {"status": "completed", "response": result}
    else:
        return {"error": result}