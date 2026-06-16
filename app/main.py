from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(host):
    return ''.join(e for e in host if e.isalnum() and e in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'invalid_input'}
    args = shlex.split(f"ping {shlex.quote(sanitized_host)}")
    subprocess.Popen(args, shell=False)
    return {'status': 'completed'}