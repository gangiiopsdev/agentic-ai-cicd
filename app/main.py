from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if 'ping' not in host or ' ' in host:
        return {'error': 'Invalid input'}
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)