from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid input'}
    return ping(host)