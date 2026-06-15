from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):  # Validate the input to prevent command injection
    if not validate_host(host):
        return {'error': 'Invalid host'}, 403
    args = ['ping', subprocess.list2cmdline([host])]  # Use list2cmdline for Windows compatibility
    subprocess.run(args, check=True)
    return {'status': 'completed'}