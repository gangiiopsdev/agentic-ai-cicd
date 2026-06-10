from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 64:
        return False
    try:
        cmd = ['ping', host]  # Directly use the host as an argument rather than splitting it
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        return False

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)