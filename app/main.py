from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> str:
    try:
        # Validate and sanitize host input
        if not all(c.isalnum() or c in '.-_' for c in host):
            raise ValueError("Invalid host")
        args = shlex.split(f'ping {host}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except (subprocess.CalledProcessError, ValueError) as e:
        return str(e).decode('utf-8')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}