from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not all(c.isalnum() for c in host) or '.' not in host:
            return {'status': 'failed', 'error': 'Invalid host'}
        cmd = ['ping', '-c', '4'] + shlex.split(host)
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)