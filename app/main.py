from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):
        return "Invalid host"
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "message": result}