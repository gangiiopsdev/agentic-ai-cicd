from fastapi import FastAPI
import subprocess
import re

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    try:
        args = ['ping', '-c', '4', host]  # Limit the number of pings for security
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    return safe_ping(host)