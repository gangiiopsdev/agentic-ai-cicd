from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation and error handling
    if not host or len(host) > 255 or any(char in host for char in [';', '&', '|', '`', '>', '<', '*', '?', '~', '{', '}', '[', ']', '\']):
        raise ValueError('Host parameter is invalid')
    try:
        subprocess.run(['ping', '127.0.0.1'], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}