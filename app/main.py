from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Using subprocess.Popen instead of subprocess.call with full path
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()} 

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's a valid IP address or hostname
    if not re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', host) and not re.match(r'^([a-zA-Z0-9]([-a-zA-Z0-9]*[a-zA-Z0-9])?)\.[a-zA-Z0-9]([-a-zA-Z0-9]*[a-zA-Z0-9])?$', host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)