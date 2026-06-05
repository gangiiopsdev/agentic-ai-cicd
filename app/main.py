from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'result': 'Invalid host'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}
def is_valid_host(host):
    # Implement validation logic here
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts