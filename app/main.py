from fastapi import FastAPI, Depends
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str = Depends(validate_host)):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode('utf-8')}
def validate_host(host: str):
    # Validate and sanitize host input
    if not is_valid_hostname(host):
        raise ValueError("Invalid hostname")
    return host
def is_valid_hostname(hostname: str) -> bool:
    # Implement validation logic here
    return True  # Placeholder implementation