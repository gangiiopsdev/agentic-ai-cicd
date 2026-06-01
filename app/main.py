from fastapi import FastAPI
import subprocess
import shlex
import re
def escape_shell(s):
    return ''.join(c if c.isalnum() or c in '_-./:' else '_' for c in s)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9._%-]+$', host):
        return {'status': 'error', 'message': 'Invalid input'}
    host = escape_shell(host)
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}