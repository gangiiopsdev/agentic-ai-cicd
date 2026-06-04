from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        raise ValueError('Invalid host name')
    # Secure implementation
    try:
        subprocess.run(['ping', host], shell=False, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)