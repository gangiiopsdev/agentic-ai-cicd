from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=5)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    # Validate the host input to prevent injection attacks
    if not host.replace('.', '').isdigit():
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)