from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Sanitize input
        if not host.strip().isalnum():
            raise ValueError('Invalid host name')
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)