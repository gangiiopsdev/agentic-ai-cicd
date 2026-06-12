from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"error": "Invalid host"}, 400
    args = ['ping', shlex.quote(host)]
    try:
        subprocess.run(args, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}, 500
    return {"status": "completed"}