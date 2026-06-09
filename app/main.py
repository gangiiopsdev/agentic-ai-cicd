from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        if not host.isdigit():  # Validate input to prevent command injection
            raise ValueError('Invalid input for host')
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}