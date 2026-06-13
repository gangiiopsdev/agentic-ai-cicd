from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def is_safe_host(host):
    safe_hosts = ['example.com', 'localhost']  # Replace with actual safe hosts
    return host in safe_hosts

@app.post('/ping')
def ping(request: PingRequest, background_tasks: BackgroundTasks):
    if not is_safe_host(request.host):
        return {'status': 'error', 'output': 'Unauthorized host'}
    try:
        output = subprocess.check_output(['ping', request.host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e.output)}
    except Exception as e:
        return {'status': 'error', 'output': str(e)}