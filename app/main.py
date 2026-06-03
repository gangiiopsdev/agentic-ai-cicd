from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host: str):
    try:
        # Use shlex.quote to sanitize the host input
        output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()
def sanitize_input(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input")
    return host

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    return run_ping(sanitized_host)