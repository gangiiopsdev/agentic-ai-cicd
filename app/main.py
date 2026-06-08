from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() or e.isspace())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.call(args)
    return {"status": "completed"}