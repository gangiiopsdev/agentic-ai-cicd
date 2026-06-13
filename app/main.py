from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in ('-', '.', ':') for c in host):
        return {'status': 'failed', 'error': 'Invalid characters in input'}
    try:
        # Use shlex.quote to safely quote the host argument
        result = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}