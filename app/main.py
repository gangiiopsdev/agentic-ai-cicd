from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent shell injection
    if not host.strip() or not all(c.isalnum() for c in host):
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}