from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe to use in a ping command
    allowed_hosts = ['localhost', '127.0.0.1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host is not allowed'}
    return safe_ping(host)