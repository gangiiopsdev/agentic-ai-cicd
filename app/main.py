from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return all(char in allowed_chars for char in host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host provided"}
    try:
        output = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}