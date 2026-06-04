from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host not in ['localhost', '127.0.0.1']:
        raise ValueError("Invalid host")
    subprocess.call(f'ping {host}', shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}