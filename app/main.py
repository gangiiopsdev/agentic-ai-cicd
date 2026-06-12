from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    import re
    host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    if '@' in host or '|' in host:
        return {'status': 'failed', 'error': 'Invalid characters detected'}
    return safe_ping(host)