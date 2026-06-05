from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    # Add validation logic here, e.g., regex match for allowed characters
    return 'localhost' in host

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}