from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping/{host}')
def ping(host: str):
    # Sanitize host input before using it in the command
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}