from fastapi import FastAPI
import subprocess
def validate_host(host: str):
    if not host.isalnum() or '.' not in host:
        return False
    return True
def execute_ping(host: str):
    if not validate_host(host):
        return 'Invalid host'
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = execute_ping(host)
    return {'status': 'completed', 'output': output}