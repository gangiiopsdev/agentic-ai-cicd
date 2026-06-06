from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Sanitize host input more thoroughly using shlex.split
        parts = shlex.split(host)
        if len(parts) != 1 or not all(c.isalnum() or c in ('.', '-', '_') for c in parts[0]):
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', '-c', '1'] + parts, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_route(host: str):
    # Ensure host input is sanitized to prevent command injection
    parts = shlex.split(host)
    if len(parts) != 1 or not all(c.isalnum() or c in ('.', '-', '_') for c in parts[0]):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(' '.join(parts))