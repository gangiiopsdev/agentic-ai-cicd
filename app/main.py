from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(lambda x: x in allowed_chars, host))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}