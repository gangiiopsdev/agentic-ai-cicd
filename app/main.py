from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        output = subprocess.run(['ping', '-c 1', f'{host}'], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}