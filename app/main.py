from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host'}, 400
    result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}