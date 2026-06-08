from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Implement appropriate sanitization logic here
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda char: char in allowed_chars, host))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {"status": "invalid host"}
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}