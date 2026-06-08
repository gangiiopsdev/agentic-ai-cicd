from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        command = ['ping', '-c', '1', host]
        subprocess.call(command, shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 403