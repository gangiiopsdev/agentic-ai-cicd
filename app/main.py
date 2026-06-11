from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return shlex.quote(host)

def safe_ping_command(host):
    command = ['ping', host]
    escaped_command = [shlex.quote(arg) for arg in command]
    return escaped_command

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(safe_ping_command(host), timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode()}