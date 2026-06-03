from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Validate and sanitize the host input
        if not isinstance(host, str) or '..' in host or '\' in host or '/' in host:
            raise ValueError('Invalid host format')
        subprocess.call(['ping', host])
    except Exception as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)