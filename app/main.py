from fastapi import FastAPI
import subprocess
import re
def safe_ping(host):
    # Validate host input to ensure it does not contain malicious content
    if not host or 'ping' in host.lower() or re.search(r'[<>|&]', host):
        raise ValueError('Invalid host input')
    return host.strip()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', safe_ping(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}