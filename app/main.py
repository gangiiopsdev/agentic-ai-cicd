from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_route(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex matching allowed hosts
    return True