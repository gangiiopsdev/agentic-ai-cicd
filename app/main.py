from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if '@' in host or '>' in host:
        raise ValueError('Unsafe input detected')
    command = ['ping', '-c 1', host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)