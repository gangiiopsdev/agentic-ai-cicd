from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum() or '-' not in host:
        raise ValueError('Invalid host format')
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}