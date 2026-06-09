from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host parameter to prevent command injection
    if not all(c.isalnum() or c in '.-' for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}

    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)