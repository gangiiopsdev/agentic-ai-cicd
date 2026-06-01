from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Ensure host is a valid IP address or hostname
    if '.' in host or ':' in host:
        return True
    return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, result.args, output=result.stderr)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}