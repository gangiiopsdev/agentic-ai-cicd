from fastapi import FastAPI
import subprocess
def safe_ping(host):
    cmd = ['ping', host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
global app
app = FastAPI()
@app.get('/ping/{host}')
def ping_endpoint(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=400, detail='Invalid host name')
    return safe_ping(host)
def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts