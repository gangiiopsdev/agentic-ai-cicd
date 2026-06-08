from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Sanitize the host input
        if not all(char.isalnum() for char in host) or len(host) > 255:
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'status': 'failed'}

app = FastAPI()

@app.get('/ping')
def ping_handler(host: str):
    try:
        # Sanitize the host input
        if not all(char.isalnum() for char in host) or len(host) > 255:
            raise ValueError('Invalid hostname')
        return ping(host)
    except ValueError as e:
        return {'error': str(e), 'status': 'failed'}