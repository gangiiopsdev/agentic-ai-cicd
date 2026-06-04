from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.isdigit():
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid input for ping')

@app.get="/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}