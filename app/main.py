from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'localhost']  # Add your allowed hosts here

def validate_host(host):
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}