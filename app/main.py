from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], shell=False, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)