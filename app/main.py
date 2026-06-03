from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run and shlex.split
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_wrapper(host: str):
    if '@' in host or '>' in host or '<' in host or '&' in host or ';' in host or '|' in host or '`' in host:
        return {'status': 'failed', 'error': 'Invalid characters in host'}
    return ping(host)