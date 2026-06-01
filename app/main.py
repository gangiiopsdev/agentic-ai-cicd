from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.strip() == 'localhost' or host.strip().startswith('127.0.0.1'):
        return True
    else:
        return False

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}