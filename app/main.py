from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail='Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}