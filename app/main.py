from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 64:
        return {'status': 'failed', 'error': 'Invalid host name'}

    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}