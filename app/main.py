from fastapi import FastAPI
import subprocess
def sanitize_input(input):
    return ''.join(c for c in input if c.isalnum() or c in ['-', '.', '_', ''])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}