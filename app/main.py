from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        return {'error': 'Invalid input'}
    result = subprocess.run(f'ping {shlex.quote(host)}', capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}