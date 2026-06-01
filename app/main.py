from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host == 'localhost' or host.startswith('127.0.0.'):  # Example of a safe check, customize as needed
        try:
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}