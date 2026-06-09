from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_argument(arg):
    return shlex.quote(arg)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and escape input to prevent injection attacks
    if not host.isalnum() or len(host) > 64:
        return {'status': 'failed', 'error': 'Invalid host'}
    escaped_host = escape_shell_argument(host)
    try:
        result = subprocess.run(['ping', escaped_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}