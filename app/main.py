from fastapi import FastAPI
import subprocess
global host_validator
host_validator = set(['example.com', 'another-example.com'])

def validate_host(host):
    return host in host_validator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}