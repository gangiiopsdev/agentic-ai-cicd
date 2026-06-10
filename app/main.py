from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.strip() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host input'}
    try:
        subprocess.check_call(['ping', host], shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}