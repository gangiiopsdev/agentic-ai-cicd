from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping_endpoint(host: str):
    if all(c.isalnum() or c in ['-', '.', '_'] for c in host):  # Enhanced validation to prevent shell injection
        return ping(host)
    else:
        return {'status': 'error', 'message': 'Invalid input'}