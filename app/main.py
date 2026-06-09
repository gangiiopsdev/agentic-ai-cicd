from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_subprocess(command, *args):
    cmd = [command] + list(args)
    for i, arg in enumerate(cmd):
        if isinstance(arg, str) and any(c.isalnum() or c in '.-_' for c in arg):
            continue
        elif isinstance(arg, str):
            cmd[i] = quote(arg)
    return subprocess.run(cmd, check=True, capture_output=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to ensure it does not contain malicious characters
    if not all(c.isalnum() or c in '.-_' for c in host):
        return {'error': 'Invalid host'}, 400
    safe_host = quote(host)
    result = safe_subprocess('ping', '-c', '1', safe_host)
    return {'status': 'completed'}