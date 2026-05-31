from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if 'ping' in host or ';' in host or '&' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}