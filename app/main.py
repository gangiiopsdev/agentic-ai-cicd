from fastapi import FastAPI
import subprocess
import re

def safe_subprocess(command, args):
    full_command = [command] + list(map(shlex.quote, args))
    result = subprocess.run(full_command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or '@' in host or '/' in host:
        return {'error': 'Invalid input'}
    return safe_subprocess('ping', ['-c', '1', shlex.quote(host)])