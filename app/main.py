from fastapi import FastAPI, Depends
import subprocess
global_hosts = {'host1', 'host2'}
app = FastAPI()
def validate_host(host: str):
    if host not in global_hosts:
        raise ValueError('Invalid host')
    return host@app.get("/ping")async def ping(host: str = Depends(validate_host)):
    try:
        result = subprocess.run(["ping", "-c 1", host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}