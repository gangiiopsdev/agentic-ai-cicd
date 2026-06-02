from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Enhanced validation and sanitization
    if not host.isnumeric() or len(host) > 15:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}