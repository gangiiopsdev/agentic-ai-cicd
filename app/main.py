from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Basic check to allow only alphanumeric characters and a few special characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}