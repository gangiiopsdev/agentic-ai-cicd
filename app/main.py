from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError('Invalid host name')
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output.decode('utf-8')}'

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    else:
        return {'status': result}