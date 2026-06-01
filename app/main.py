from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input
        if not all(c.isalnum() or c in '.-' for c in host):
            return {'status': 'error', 'output': 'Invalid hostname'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}