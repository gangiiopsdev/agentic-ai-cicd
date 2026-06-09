from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Basic validation, more complex checks may be necessary
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', f'-c 1 {host}']  # Limit the number of pings to avoid potential abuse
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}