from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def shell_quote(s):
    return ''.join(['\', c] if c in '\"$`' else c for c in s)

@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host'}, 400

    subprocess.run(['ping', shell_quote(host)], check=True)
    return {'status': 'completed'}