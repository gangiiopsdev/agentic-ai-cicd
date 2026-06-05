from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # List of allowed hosts
    if host not in allowed_hosts:
        raise HTTPException(status_code=400, detail='Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except HTTPException as e:
        raise e
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}