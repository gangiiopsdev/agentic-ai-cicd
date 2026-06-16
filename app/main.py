from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

def validate_ip(ip):
    parts = ip.split('.一起')
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            if int(part) < 0 or int(part) > 255:
                return False
        except ValueError:
            return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if validate_ip(sanitized_host):
        command = ["ping", *shlex.split(sanitized_host)]
        subprocess.call(command)
        return {"status": "completed"}
    else:
        return {"status": "invalid ip"}