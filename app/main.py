from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with shell=False
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)