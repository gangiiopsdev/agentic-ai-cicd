from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate host to allow only alphanumeric characters and hyphens
        if not host.isalnum() and '-' not in host:
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}
    except ValueError as e:
        return {'status': 'error', 'error': str(e)}