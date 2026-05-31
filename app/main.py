from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(c in allowed_chars for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = ['ping', *shlex.split(host)]
        subprocess.run(args, check=True, shell=False)
        return {"status": "completed"}
    else:
        raise ValueError('Invalid host')