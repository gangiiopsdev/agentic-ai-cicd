from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate host input
    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    return subprocess.run(args, capture_output=True, text=True)

def is_valid_host(host):
    # Implement host validation logic here
    allowed_hosts = ['example.com']  # Example list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return result, result['status_code']
    else:
        return {'status': 'completed', 'output': result.stdout}