from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        raise ValueError(f'Host {host} is not allowed')
    # Secure implementation using subprocess.run with shell=False and arguments passed as a list
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}