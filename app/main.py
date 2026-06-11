from fastapi import FastAPI
import subprocess
git_path = '/usr/bin/ping'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Use a safe implementation to avoid command injection
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.run([git_path, '-c', '1', '--', host], check=True)
    return {'status': 'completed'}