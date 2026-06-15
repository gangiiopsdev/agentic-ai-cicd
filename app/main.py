from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']

def safe_host_validation(host):
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):    if safe_host_validation(host):
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'result': result.stdout.strip()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}    else:
        return {'status': 'error', 'message': 'Invalid host'}