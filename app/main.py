from fastapi import FastAPI
import subprocess
import re
import shlex

def escape_shell(s):
    return ''.join(c if c.isalnum() or c in '_-./:' else '_' for c in s)

def validate_and_escape_host(host):
    if not re.match(r'^[a-zA-Z0-9._%-]+$', host):
        raise ValueError('Invalid input')
    return escape_shell(host)

app = FastAPI()

@app.get('/ping')
async def ping(host: str):
    try:
        host = validate_and_escape_host(host)
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}