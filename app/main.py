from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or '&&' in host or ';' in host:
        raise ValueError('Invalid input')
    subprocess.run(['ping', f'-c 1 {host}'], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}