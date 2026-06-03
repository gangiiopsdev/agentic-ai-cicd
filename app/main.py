from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_host(host):
    return quote(host)

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize input to prevent command injection
        if not host.isalnum() and '-' not in host:
            raise ValueError('Invalid host format')
        output = subprocess.check_output(['ping', escape_host(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}