from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        try:
            subprocess.run(['ping', host], check=True)
            return True
        except subprocess.CalledProcessError as e:
            return False
    return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed", "error": "Host not allowed"}