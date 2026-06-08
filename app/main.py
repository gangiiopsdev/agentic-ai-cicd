from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize the input by whitelisting allowed hosts or using a safer method
        if host not in ['allowed_host1', 'allowed_host2']:
            return {'status': 'error', 'message': 'Invalid host'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}