from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    # Simple example of validation, replace with more robust logic as needed
    return host.replace('.', '').replace('-', '').isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}