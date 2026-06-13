from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(ch for ch in input_str if ch.isalnum() or ch in '._-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.run(["ping", sanitized_host], check=True)
    return {"status": "completed"}