from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    if not host.isalnum() or '-' not in host:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        args = ['ping', shlex.quote(sanitized_host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError as e:
        return {'status': 'error', 'output': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}