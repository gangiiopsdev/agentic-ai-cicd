from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Secure implementation using subprocess.run with a list of arguments and input validation
    try:
        if not all(c.isalnum() or c in '-.' for c in host):  # Simple validation, not perfect but better than nothing
            return {'status': 'failed', 'error': 'Invalid host name'}
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)