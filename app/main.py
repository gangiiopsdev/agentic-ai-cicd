from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    if host.startswith('192.168.') or host.startswith('10.'):  # Example of a whitelist
        return ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}