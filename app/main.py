from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host:
        raise ValueError("Host cannot be empty")
    subprocess.call(['ping', host])

@app.get="/ping")
def ping(host: str):
    try:
        return {"status": "completed", "output": safe_ping(host)}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}