from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Use shlex to safely quote the host argument
        args = ['ping'] + shlex.split(host)
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    # Validate input to ensure it does not contain unexpected characters or commands
    if not host.isalnum() and '-' not in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)