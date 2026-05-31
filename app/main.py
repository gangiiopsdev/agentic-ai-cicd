from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError("Invalid input")
    command = shlex.split('ping ' + sanitized_host)
    subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed"}