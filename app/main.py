from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate the host to ensure it's a valid domain or IP address
        if not (host.strip() and re.match(r'^[a-zA-Z0-9.-]+$', host)):
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)