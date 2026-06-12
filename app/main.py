from fastapi import FastAPI
import subprocess
from shlex import quote

def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitized_input(host))
    subprocess.run(f'ping {sanitized_host}', shell=False, check=True)
    return {"status": "completed"}