from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    # Use shlex to safely handle user input
    result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}