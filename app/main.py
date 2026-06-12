from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Define a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)