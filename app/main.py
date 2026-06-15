from fastapi import FastAPI
import subprocess
global _ping_command_cache = {}

app = FastAPI()

def validate_host(host):
    if not host.isdigit():
        raise ValueError('Invalid host input')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        if host not in _ping_command_cache:
            _ping_command_cache[host] = ['ping', host]
        subprocess.call(_ping_command_cache[host])
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}, 400