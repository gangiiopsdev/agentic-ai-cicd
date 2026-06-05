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
    subprocess.call(command, shell=False)  # Explicitly set shell to False
    return {'status': 'completed'}