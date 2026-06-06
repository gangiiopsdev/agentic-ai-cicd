from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if host not in ['localhost', '127.0.0.1']:
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)