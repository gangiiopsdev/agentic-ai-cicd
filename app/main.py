from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in allowed_chars for char in host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):\n    if not validate_host(host):\n        raise ValueError("Invalid hostname")\n    args = shlex.split(f'ping {shlex.quote(host)}')\n    subprocess.run(args, check=True)\n    return {"status": "completed"}