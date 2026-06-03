from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not is_safe_host(host):
        return {"error": "Unsafe host"}, 403
    try:
        subprocess.call(["ping", host], shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500
def is_safe_host(host: str):
    # Implement logic to check if the host is safe
    allowed_hosts = ["example.com", "another.example.com"]
    return host in allowed_hosts

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)