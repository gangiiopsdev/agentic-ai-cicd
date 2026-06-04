from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize the input to prevent command injection
    parts = host.split()
    safe_host = ' '.join([quote(part) for part in parts])
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
global app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)