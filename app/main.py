from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    cmd = ['ping'] + [arg for arg in host.split(' ') if arg.isalnum()]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)