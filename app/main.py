from fastapi import FastAPI
import subprocess
app = FastAPI()
def safe_ping(host: str):
    # Enhanced validation to prevent shell injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host): raise ValueError('Invalid host name')
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    # Safe implementation using subprocess.run with a full path to avoid potential shell injection
    result = subprocess.run(["/bin/ping", host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}