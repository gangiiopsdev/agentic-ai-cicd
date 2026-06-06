from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host to prevent command injection
    if not all(c.isalnum() or c in ['-', '.'] for c in host):  # Simple validation, may need more comprehensive checks
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        result = subprocess.run(['ping', host], check=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)