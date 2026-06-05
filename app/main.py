from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in host if char in allowed_chars)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.call(['ping', f'"{sanitized_host}"'])  # Adding quotes around the host
    return {"status": "completed"}