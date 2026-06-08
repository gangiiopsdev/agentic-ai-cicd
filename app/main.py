from fastapi import FastAPI
import subprocess

def escape_host(host):
    return ''.join(e for e in host if e.isalnum() or e in ('.', '-', '_'))

def sanitize_command(command):
    return ' '.join(subprocess.list2cmdline(arg) for arg in command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    command = ['ping', escaped_host]
    sanitized_command = sanitize_command(command)
    subprocess.call(sanitized_command, shell=False)
    return {"status": "completed"}