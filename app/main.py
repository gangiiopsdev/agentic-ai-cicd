from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    # Example validation logic, replace with actual validation
    return host.isalnum()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', host]
    subprocess.run(command, check=True)  # Use subprocess.run instead of subprocess.call
    return {'status': 'completed'}