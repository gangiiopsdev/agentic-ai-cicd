from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Ping failed with error: {e.stderr}"

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)