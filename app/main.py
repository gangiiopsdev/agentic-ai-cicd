from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host to ensure it does not contain unexpected characters
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'error', 'error': str(ve)}