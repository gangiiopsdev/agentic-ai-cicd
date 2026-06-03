from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com']
    if host in allowed_hosts:
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)