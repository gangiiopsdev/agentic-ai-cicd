from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', '127.0.0.1']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}
    else:
        return {'status': 'error', 'error': 'Host not allowed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if all(char in host for char in ['.', '-', '_', '0-9']) and len(host.split('.')) == 4:
        return safe_ping(host)
    else:
        return {'status': 'error', 'error': 'Invalid host'}