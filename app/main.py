from fastapi import FastAPI
import subprocess
global host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400

    try:
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500