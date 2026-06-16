from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    try:
        # Regular expression to allow only valid characters in host input
        if re.match(r'^[a-zA-Z0-9.-_]+$', host) is None:
            return {'status': 'failed', 'error': 'Invalid host input'}
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)