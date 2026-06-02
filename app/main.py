from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    valid_hosts = ['example.com', 'test.com']
    if host not in valid_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)