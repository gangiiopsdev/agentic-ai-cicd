from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.startswith('192.168.') or host.startswith('10.'):  # Example safe subnet checks
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}, 400