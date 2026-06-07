from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    return host if host in allowed_hosts else '127.0.0.1'

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    result = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}