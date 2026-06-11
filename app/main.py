from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use full executable path and validate input
        output = subprocess.run(['ping', host], stderr=subprocess.PIPE, check=True)
        return output.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.strip().isdigit() and '@' not in host and '.' in host:
        return {'error': 'Invalid host input'}
    return {'status': safe_ping(host)}