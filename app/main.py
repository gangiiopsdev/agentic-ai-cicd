from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    # Implement validation logic here (e.g., allow only certain hosts)
    allowed_hosts = ['host1', 'host2']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    try:
        # Use shlex.quote to safely escape the command arguments
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}