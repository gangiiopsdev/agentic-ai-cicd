from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if 'ping' not in host or '..' in host:
        raise ValueError('Invalid host')
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout + result.stderr}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}