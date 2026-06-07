from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isascii() and all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host)

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Invalid input')