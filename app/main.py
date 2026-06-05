from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host')
    return subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}