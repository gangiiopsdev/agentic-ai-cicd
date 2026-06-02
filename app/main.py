from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Basic validation: check for disallowed characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host])
    else:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed'}