from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    return host if host in allowed_hosts else '127.0.0.1'

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = [os.path.join(os.environ['PATH'], 'ping'), sanitized_host]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}