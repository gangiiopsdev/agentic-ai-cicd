from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Add more allowed hosts as needed
    return host in allowed_hosts

app = FastAPI()

@app.get="/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(["ping", host], check=True, shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}