from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid hostname")
    safe_host = shlex.quote(host)
    result = subprocess.run(["ping", "-c", "1", safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}