from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate input to ensure it does not contain harmful characters or commands
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if any(char not in allowed_chars for char in host):
        raise ValueError('Invalid hostname')

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)