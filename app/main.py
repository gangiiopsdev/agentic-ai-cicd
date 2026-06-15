from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    # Implement validation logic here (e.g., allow only known hosts)
    return host in ['example.com', 'test.com']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}