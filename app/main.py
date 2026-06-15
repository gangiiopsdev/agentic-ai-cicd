from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['google.com', 'example.com']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)