from fastapi import FastAPI
import subprocess
def validate_host(host: str):
    # Use a more comprehensive and secure method to validate the host
    return True  # Placeholder for actual validation logic

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}