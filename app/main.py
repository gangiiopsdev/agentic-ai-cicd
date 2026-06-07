from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example allowed hosts
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):  # Validate the host input
        command = [os.path.realpath('ping'), host]
        subprocess.run(command, check=True)
        return {"status": "completed"}
    else:
        raise ValueError("Invalid host")