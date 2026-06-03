from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}