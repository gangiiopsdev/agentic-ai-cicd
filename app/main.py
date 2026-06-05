from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(c in allowed_chars for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(['ping'] + shlex.split(host), check=True, stdout=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    else:
        return {"status": "error", "message": "Invalid host name"}