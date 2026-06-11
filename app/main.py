from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host: str):
    try:
        args = ['ping', host]
        output = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return run_ping(host)

def is_valid_host(host: str) -> bool:
    allowed_hosts = ['localhost', '127.0.0.1']  # Add more allowed hosts as needed
    return host in allowed_hosts