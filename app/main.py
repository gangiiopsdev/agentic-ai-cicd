from fastapi import FastAPI
import subprocess
def validate_host(host):
    if 'ping' in host:
        return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid input detected'}, 400
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}