from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the input
        if not host or ' ' in host or '@' in host:
            raise ValueError('Invalid host input')
        subprocess.run(['ping', '-c', '1', host], check=True)
        return {'status': 'completed'}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'error', 'message': str(e)}