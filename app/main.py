from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if 'ping' in host.split():
        return "Invalid input"
    result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):    
    return safe_ping(host)