from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return ''.join(c for c in arg if c.isalnum() or c in ' .-_/')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    safe_host = escape_shell_arg(host)
    args = shlex.split(f'ping {safe_host}')
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed'}