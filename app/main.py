from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run without shell=True
    try:
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {'status': 'success'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)