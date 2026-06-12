from fastapi import FastAPI
import asyncio
from subprocess import run, PIPE

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        result = run(['ping', host], stdout=PIPE, stderr=PIPE, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    return ping(host)