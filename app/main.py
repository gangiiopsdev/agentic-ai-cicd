from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shlex.split for safe command execution
    subprocess.run(shlex.split(f'ping {host}')), check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    ping(host)
    return {"status": "completed"}