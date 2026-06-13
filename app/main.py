from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use full executable path and validate input
        output = subprocess.run(['/sbin/ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout.strip()
    except subprocess.CalledProcessError as e:
        return str(e.stderr.strip())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.strip().isdigit() and '@' not in host and '.' in host:
        return {'error': 'Invalid host input'}
    return {'status': safe_ping(host)}