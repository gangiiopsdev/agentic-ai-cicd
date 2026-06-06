from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Validate input
    if not host or 'localhost' in host:
        return {'status': 'error', 'message': 'Invalid host'}

    # Secure implementation
    try:
        args = ['ping', '-c', '1', host]
        subprocess.run(args, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)