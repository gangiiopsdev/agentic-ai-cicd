from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        cmd = ['ping', host]
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return e.stderr.decode()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.isalnum() and '.' in host:
        return safe_ping(host)
    else:
        return {"error": "Invalid host name"}