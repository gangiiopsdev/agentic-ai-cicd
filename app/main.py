from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    # Safe implementation using subprocess.run
    subprocess.run(['ping', '-c 1', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500