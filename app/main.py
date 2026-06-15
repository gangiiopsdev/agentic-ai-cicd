from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.replace('.', '').isdigit() or len(host.split('.')) != 4:
        return {'status': 'error', 'message': 'Invalid IP address'}
    return safe_ping(host)