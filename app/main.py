from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)