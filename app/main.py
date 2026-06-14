from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.strip() == '127.0.0.1':
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        raise ValueError("Invalid host")

    # Safe implementation
    subprocess.call(f"ping {host}", shell=False)

    return {"status": "completed"}