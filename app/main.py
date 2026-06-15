from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example list of allowed hosts
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host], shell=False)
    else:
        return {"status": "invalid host"}
    
    return {"status": "completed"}