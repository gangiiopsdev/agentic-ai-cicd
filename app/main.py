from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host in ['example.com', 'test.com']

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], check=True)

    return {"status": "completed"}