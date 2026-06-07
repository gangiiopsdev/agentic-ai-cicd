from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    # Safer implementation using subprocess.run with args parameter and shell=False
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return {'result': ping(host)}
    except subprocess.CalledProcessError as e:
        return {'error': str(e.output.decode('utf-8'))}