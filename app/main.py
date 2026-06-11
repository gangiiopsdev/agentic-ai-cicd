from fastapi import FastAPI
import subprocess
def safe_subprocess(command, *args, **kwargs):
    return subprocess.run([command] + list(args), capture_output=True, text=True)

app = FastAPI()
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    result = safe_subprocess('ping', '-c 1', sanitized_host)
    return {'status': result.stdout}