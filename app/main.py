from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate the host input before using it in the command
        if not all(c.isalnum() or c in ['.', '-'] for c in host):
            raise ValueError('Invalid characters in host input')
        result = subprocess.run(['ping', '--', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping_endpoint(host: str):
    if host.isalnum():  # Basic validation to prevent shell injection
        return ping(host)
    else:
        return {'status': 'error', 'message': 'Invalid input'}