from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.strip().isalnum():
        return {'status': 'error', 'output': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping'] + shlex.split(host), check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}