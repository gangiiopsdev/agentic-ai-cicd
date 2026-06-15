from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed' if result.returncode == 0 else 'failed', 'message': result.stdout}