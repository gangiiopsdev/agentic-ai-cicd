from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['example.com', '127.0.0.1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_safe_hosts:
        subprocess.call(['ping', host])
    else:
        return {"error": "Host not allowed"}
    return {"status": "completed"}