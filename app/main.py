from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return all(c.isalnum() or c in [".", "-"] for c in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid hostname'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}