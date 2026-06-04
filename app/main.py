from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> dict:
    try:
        args = shlex.split(f'ping -c 1 {host}')  # Limit the number of pings for security
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)