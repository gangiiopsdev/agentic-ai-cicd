from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = {'example.com', 'test.com'}

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        # Secure implementation
        subprocess.call(["ping", "/bin/ping", host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}