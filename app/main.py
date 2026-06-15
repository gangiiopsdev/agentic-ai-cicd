from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(ch if ch.isalnum() or ch in ['-', '.', '_', '@'] else '_' for ch in host)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}", shell=True)
    return {"status": "completed"}