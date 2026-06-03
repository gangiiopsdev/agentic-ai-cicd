from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with input validation and sanitization
    if not is_valid_host(host):
        return {'status': 'invalid host'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    return all(c.isalnum() or c in ('.', '-') for c in host)