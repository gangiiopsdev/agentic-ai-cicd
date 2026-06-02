from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_command(cmd):
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Whitelist of allowed hosts
    allowed_hosts = ["127.0.0.1", "localhost"]
    if host in allowed_hosts:
        return run_safe_command(["ping", host])
    else:
        return {"status": "host not allowed"}