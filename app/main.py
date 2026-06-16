from fastapi import FastAPI
import subprocess

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

def validate_host(host):
    valid_hosts = ['example.com', 'test.example.net']  # Example list of valid hosts
    return host in valid_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "output": "Invalid host name"}
    sanitized_host = sanitize_host(host)
    try:
        result = subprocess.run(["ping", "/bin/ping", sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}