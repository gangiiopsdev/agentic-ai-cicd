from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize user input
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', f'/bin/ping'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}