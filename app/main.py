from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_host(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    return ping_host(host)