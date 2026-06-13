from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize and validate host input
    if not valid_host(host):
        return {'status': 'invalid_host'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}

# Example validation function
def valid_host(host: str) -> bool:
    # Add your validation logic here
    return host.isalpha() and len(host) <= 255