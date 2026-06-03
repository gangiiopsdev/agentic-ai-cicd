from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {'error': 'Invalid host input'}
    try:
        # Secure implementation using subprocess.run with validation and escaping
        result = subprocess.run(['ping', '-c', '1', f'"{host}"'], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}