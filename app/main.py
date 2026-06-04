from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    return ''.join(c for c in host if c.isalnum() or c in ('.', '-', ':'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host.strip():
        return {"status": "failed", "error": "Invalid input"}
    try:
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], timeout=5, stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}