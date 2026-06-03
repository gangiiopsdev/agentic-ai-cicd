from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., check if the host is within a whitelist
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

app = FastAPI()
class PingRequest(BaseModel):
    host: str

def execute_ping(host: str) -> str:
    try:
        # Sanitize the input by using subprocess.Popen instead of subprocess.run
        result = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        return stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e)

@app.post("/ping")
def ping(request: PingRequest):
    if not validate_host(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}

    output = execute_ping(request.host)
    return {'status': 'completed', 'output': output}