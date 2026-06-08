from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if host.strip():
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'result': 'Ping successful for ' + host}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        raise ValueError('Host parameter is required')

app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)