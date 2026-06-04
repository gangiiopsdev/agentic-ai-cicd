from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        args = shlex.split(f'ping -c 1 {host}')  # Limit the number of pings to avoid excessive resource usage
        result = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)
def is_valid_host(host: str) -> bool:
    # Basic validation, can be expanded based on specific requirements
    return '.' in host and len(host.split('.')) == 4