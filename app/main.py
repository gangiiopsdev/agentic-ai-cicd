from fastapi import FastAPI
import subprocess
import shlex
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '4', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except cimport as e:
        return {'status': 'failed', 'error': e.stderr}

# Additional preventive controls:
# 1. Validate the input more strictly to ensure it only contains expected characters.
# 2. Use a whitelist of allowed hosts instead of allowing arbitrary input.
# 3. Consider using asynchronous subprocess calls if possible to avoid blocking the event loop.