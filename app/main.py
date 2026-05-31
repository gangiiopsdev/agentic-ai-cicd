from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError("Invalid input")
    subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, capture_output=True)
    return {"status": "completed"}