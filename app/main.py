from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Validate and sanitize host input
        if not host.strip() or '@' in host or '.' not in host:
            raise ValueError('Invalid host input')
        subprocess.run(['ping', host], check=True)
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)