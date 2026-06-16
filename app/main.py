from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    return ''.join(c for c in user_input if c.isalnum() or c in ['.', '-', '_', ''])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(shlex.split(f"ping {sanitized_host}"))
    return {"status": "completed"}