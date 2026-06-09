from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def ping(host: str):
    if not host:
        return {'status': 'empty input'}
    try:
        response = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'response': response.stdout}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)