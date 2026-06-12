from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        subprocess.call(["ping", f'"{host}"'])  # Sanitize the input
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400