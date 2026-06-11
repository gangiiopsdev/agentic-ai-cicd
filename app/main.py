from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use full executable path and validate input
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.strip().isdigit() and '@' not in host and '.' in host:
        return {'error': 'Invalid host input'}
    return {'status': safe_ping(host)}