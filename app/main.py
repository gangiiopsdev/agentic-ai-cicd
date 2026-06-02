from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}