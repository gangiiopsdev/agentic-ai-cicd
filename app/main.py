from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.strip() not in ['localhost', '127.0.0.1']:
        raise ValueError("Invalid host")
    subprocess.call(['ping', host])

@app.get="/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}