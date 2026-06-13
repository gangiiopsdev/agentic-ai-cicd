from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1'] + shlex.split(sanitized_host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}