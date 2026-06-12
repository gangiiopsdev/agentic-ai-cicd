from fastapi import FastAPI
import subprocess

app = FastAPI()

def _sanitize_input(host):
    return ''.join(c for c in host if c.isalnum() or c in ['-', '.', ':', '/'])

@app.get("/ping")
def ping(host: str):
    safe_host = _sanitize_input(host)
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}