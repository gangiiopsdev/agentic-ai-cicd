from fastapi import FastAPI
import shlex
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize the host input to prevent command injection
        args = shlex.split(f'ping {shlex.quote(host)}')
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}