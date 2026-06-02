from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if host.strip().endswith('example.com'):
        subprocess.call(['ping', host])
    else:
        raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    try:
        secure_ping(host)
    except Exception as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}