from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host or len(host) > 255 or '.' not in host:
        raise ValueError('Invalid host input')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}