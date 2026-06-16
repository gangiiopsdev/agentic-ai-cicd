from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(c for c in host if c in allowed_chars)

def run_ping_command(sanitized_host):
    # Secure implementation using subprocess.run with shell=False and list arguments
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    output = run_ping_command(sanitized_host)
    return {"status": "completed", "output": output}