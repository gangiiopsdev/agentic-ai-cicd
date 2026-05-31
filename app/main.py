from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in allowed_chars for char in host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid hostname")
    # Use a safe method to construct the command
    args = ["ping", shlex.quote(host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}