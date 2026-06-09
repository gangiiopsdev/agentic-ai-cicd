from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input to ensure it does not contain malicious characters
    if not host.isalnum() and '-' not in host:
        return 'Invalid host name'
    try:
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output.decode("utf-8")}'

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)