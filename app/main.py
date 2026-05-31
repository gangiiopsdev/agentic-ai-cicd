from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Validate input
    if not host:
        raise ValueError('Host parameter cannot be empty')
    for char in host:
        if char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-':
            raise ValueError('Invalid characters in host parameter')

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(['ping', secure_ping(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}