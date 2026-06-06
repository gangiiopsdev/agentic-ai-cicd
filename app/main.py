from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate and sanitize the host input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname')
        subprocess.call(['ping', host], timeout=5)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)