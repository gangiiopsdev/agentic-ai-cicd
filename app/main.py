from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        # Use a whitelist approach to validate the host input
        allowed_hosts = ['google.com', 'example.com']
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)