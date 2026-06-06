from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum() or ' ' in host:
        return {'status': 'error', 'message': 'Invalid host input'}

    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)

    return {'status': 'completed', 'output': result.stdout}