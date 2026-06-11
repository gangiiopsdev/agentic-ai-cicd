from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced validation to include allowed characters
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host) or len(host) > 255:
        raise ValueError('Invalid host parameter')
    command = ['ping', host]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}