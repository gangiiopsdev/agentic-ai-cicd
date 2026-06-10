from fastapi import FastAPI
import subprocess
cimport = subprocess.run

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        return {'error': 'Invalid input'}
    result = cimport(f'ping {shlex.quote(host)}', capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}