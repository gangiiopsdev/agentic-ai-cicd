from fastapi import FastAPI
import subprocess
cimport = ['ping']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize input to prevent injection attacks
        if not all(c.isalnum() or c in '-.' for c in host):
            return {'status': 'failed', 'error': 'Invalid input'}
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}