from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 64

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}