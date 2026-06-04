from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and validation
    try:
        # Validate input to ensure it's a valid hostname
        if not host.isalnum() or '.' not in host:
            return {'status': 'error', 'message': 'Invalid hostname'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}