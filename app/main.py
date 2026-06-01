from fastapi import FastAPI
import subprocess
def safe_subprocess(command):
    return ['ping', *command]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid hostname')
    subprocess.run(safe_subprocess([host]), check=True)
    return {'status': 'completed'}