from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate host input to prevent injection
        if not host.strip().replace('.', '').isdigit():
            return {'status': 'failed', 'error': 'Invalid host'}
        args = shlex.split(f'ping -c 1 {host}')  # Limiting the number of pings for security
        subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}