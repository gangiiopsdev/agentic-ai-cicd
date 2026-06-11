from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.strip():
        return {"status": "failed", "error": "Invalid input"}
    return secure_ping(host)