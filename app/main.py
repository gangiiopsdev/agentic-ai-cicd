from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Define a list of safe hosts
    safe_hosts = ['127.0.0.1', '::1']
    return host in safe_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 403