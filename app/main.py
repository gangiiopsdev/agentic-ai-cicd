from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': f'Ping failed with error {e}'}, 500

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    if isinstance(result, dict) and 'status' in result and result['status'] == 'error':
        return result, 500
    else:
        return {'status': 'completed'}