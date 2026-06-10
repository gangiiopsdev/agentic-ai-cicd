from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)