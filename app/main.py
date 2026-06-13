from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Secure implementation using subprocess.run with input validation
        if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': 'Invalid host'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}