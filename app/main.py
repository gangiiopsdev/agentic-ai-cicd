from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of safe hosts
    return host in allowed_hosts

def sanitize_input(user_input):
    safe_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in user_input if c in safe_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not is_safe_host(sanitized_host):
        return {"status": "error", "message": "Unsafe host"}
    try:
        subprocess.run(['ping', sanitized_host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}