from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(lambda x: x in allowed_chars, host))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {"status": "invalid input"}
    command = shlex.split(f'ping {sanitized_host}')
    subprocess.run(command, check=True)
    return {"status": "completed"}