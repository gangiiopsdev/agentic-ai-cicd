from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'reason': 'Invalid host'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if 'failed' in result:
        return result
    # Safe implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}