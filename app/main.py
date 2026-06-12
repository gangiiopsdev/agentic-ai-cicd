from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts

class PingRequest(BaseModel):
    host: str

def safe_ping(host: str):
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

@app.get("/ping")
def ping(request: PingRequest):
    if subprocess.call(['ping', request.host], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
        return {'status': 'completed', 'output': result.stdout.decode()}
    else:
        return {'status': 'failed', 'error': str(e)}