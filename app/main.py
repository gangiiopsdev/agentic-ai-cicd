from fastapi import FastAPI
import subprocess
import shlex
c = shlex

app = FastAPI()

@app.get('/ping_secure')
def ping_secure(host: str):
    if not host.replace('.', '').replace('-', '').isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = c.split(f'ping {host!r}')  # Use !r to safely escape the input
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout, 'error': result.stderr}