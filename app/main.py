from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not host or not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        args = ['ping', *shlex.split(host)]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}