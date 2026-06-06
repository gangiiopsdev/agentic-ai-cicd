from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host name'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)