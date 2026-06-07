from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        if host in ['example.com', 'localhost']:  # Replace with actual whitelist
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': 'Unauthorized host'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}