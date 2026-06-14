from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    # Implement proper sanitization logic here
    return ''.join(c for c in host if c.isalnum() or c in '.-')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = ['ping'] + shlex.split(sanitized_host)
    subprocess.call(command)
    return {"status": "completed"}