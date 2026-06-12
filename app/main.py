from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        # Validate host input to prevent injection attacks
        if not re.match(r'^[a-zA-Z0-9.-]+$', host) or len(host) > 255:
            raise ValueError('Invalid host name')
        command = ['ping'] + shlex.split(host)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)