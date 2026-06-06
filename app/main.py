from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_', '/'))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', shell_quote(sanitized_host)])
    return {"status": "completed"}