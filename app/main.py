from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to avoid command injection
    if not all(c.isalnum() or c in ['-', '.', ' '] for c in host):
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', '--'] + host.split(' ')
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}