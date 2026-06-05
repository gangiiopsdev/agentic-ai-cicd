from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it is safe to ping
    if not validate_host(host):
        return {"error": "Invalid host", "status": "failed"}
    try:
        subprocess.call(["ping", host])
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}

def validate_host(host: str) -> bool:
    # Add your validation logic here, e.g., check for allowed characters and formats
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in host)