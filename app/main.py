from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['example.com', 'test.com']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_safe_hosts:
        subprocess.call(f'ping {host}', shell=True)
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}