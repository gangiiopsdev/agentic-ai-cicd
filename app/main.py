from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to allow only alphanumeric characters and hyphens
        if not host.isalnum() and '-' not in host:
            raise ValueError('Invalid host name')
        sanitized_host = shlex.quote(host)
        output = subprocess.check_output(shlex.split(f'ping {sanitized_host}'), stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}