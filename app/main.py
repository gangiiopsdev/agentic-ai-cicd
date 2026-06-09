from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_command(host):
    return ''.join(c if c.isalnum() or c in '._-' else '_' for c in host)

def ping_safe(host: str):
    escaped_host = escape_shell_command(host)
    subprocess.call(['ping', shlex.quote(escaped_host)])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)