from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(['ping', safe_ping(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}