from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    try:
        socket.inet_aton(host)
        return True
    except socket.error:
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host) or len(host.split('.')) != 4:
        return {"error": "Invalid host"}, 400
    args = shlex.split(f'ping -c 1 {host}')
    subprocess.run(args)
    return {"status": "completed"}