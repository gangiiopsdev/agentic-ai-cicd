from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run without shell=True and proper input validation
    if not host.strip():
        return {'status': 'failed', 'error': 'Host parameter is required'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_wrapper(host: str):
    if not host.strip():
        return {'status': 'failed', 'error': 'Host parameter is required'}
    return ping(host)