from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host:
        return {'status': 'failed', 'error': 'Host is required'}
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)