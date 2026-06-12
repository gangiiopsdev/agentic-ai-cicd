from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate and sanitize the input
    if not host or len(host) > 255 or not host.replace('.', '').isnumeric():
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)