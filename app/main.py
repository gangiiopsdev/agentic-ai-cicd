from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Additional check for invalid characters
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {'status': 'error', 'message': 'Invalid host format'}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}