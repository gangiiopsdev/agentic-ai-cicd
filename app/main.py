from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Simple validation example: allow only alphanumeric characters and a few common separators
    return host.isalnum() or '.' in host or '-' in host

def execute_ping(host):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    command = ['ping', host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping(host: str):
    try:
        return execute_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}