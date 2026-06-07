from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if '@' in host or '\' in host or '>' in host or '<' in host or ';' in host or '|' in host or '&' in host or '`' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)