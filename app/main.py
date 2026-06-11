from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the hostname format
    if '@' in host:
        raise ValueError('Invalid hostname format')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': result.returncode, 'output': result.stdout}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)