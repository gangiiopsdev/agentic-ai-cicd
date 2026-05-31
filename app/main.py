from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid host name")
    command = ['ping', host]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": e.stderr
        }

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return response
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e)
        }