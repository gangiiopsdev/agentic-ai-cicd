from fastapi import FastAPI
import subprocess
given_safe_hosts = {"example.com", "localhost"}  # Define safe hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in given_safe_hosts:
        subprocess.call(f"ping {host}", shell=True)
        return {"status": "completed"}
    else:
        return {"error": "Unauthorized host"}