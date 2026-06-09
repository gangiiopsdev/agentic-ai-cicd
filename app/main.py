from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError("Invalid hostname")
    args = ['ping', '--', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}