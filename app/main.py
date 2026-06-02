from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and properly sanitized inputs
    if not host:
        return {"status": "error", "message": "Host parameter is missing"}
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if any(char not in allowed_chars for char in host):
        return {"status": "error", "message": "Invalid host parameter"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}