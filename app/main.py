from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Enhanced input validation with more robust checks
    if host.isalnum() and len(host) <= 255:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid hostname')

@app.get('/ping')
def ping_endpoint(host: str):
    try:
        return {'result': ping(host)}
    except ValueError as e:
        return {'error': str(e)}