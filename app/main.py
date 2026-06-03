from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent shell injection
    if not host.isalnum():
        return {'error': 'Invalid input'}
    return safe_ping(host)