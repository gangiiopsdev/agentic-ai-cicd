from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host to ensure it only contains expected characters
    if not host.replace('.', '').isnumeric() or len(host.split('.')) != 4:
        return {'status': 'error', 'message': 'Invalid host'}

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}