from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        # Validate the host parameter to ensure it's a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', safe_host):
            return {'status': 'failed', 'error': 'Invalid host parameter'}
        result = subprocess.run(['ping', '-c', '1'] + [safe_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}