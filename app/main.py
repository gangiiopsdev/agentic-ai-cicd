from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    command = f'ping {escaped_host}'
    args = shlex.split(command)
    subprocess.run(args, check=True)
    return {"status": "completed"}