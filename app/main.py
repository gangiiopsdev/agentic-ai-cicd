from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.replace('.', '').isnumeric() or '.' not in host:
        return {'status': 'invalid', 'message': 'Invalid host address'}
    return safe_ping(host)