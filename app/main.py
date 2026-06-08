from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)