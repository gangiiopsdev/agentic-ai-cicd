from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return all(c.isalnum() or c in [".", "-"] for c in host)

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid hostname'}
    return safe_ping(host)