from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}