from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if host.strip() not in ['localhost', '127.0.0.1']:
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}