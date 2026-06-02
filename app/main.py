from fastapi import FastAPI
import subprocess
def secure_ping(host):
    valid_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in valid_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'error': str(e)}