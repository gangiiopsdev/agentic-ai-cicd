from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host:
        raise ValueError('Host parameter is required')
    # Sanitize input to prevent command injection using shlex.quote
    args = ['ping'] + shlex.split(shlex.quote(host))
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}