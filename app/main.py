from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with validation
    allowed_hosts = ['example.com', '192.168.0.1']  # Add more allowed hosts as needed
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)