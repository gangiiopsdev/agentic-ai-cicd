from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', safe_ping(host)], timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}