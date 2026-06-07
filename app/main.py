from fastapi import FastAPI
import subprocess
import re

class Ping:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        # Safe implementation
        args = ['ping', self.host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid hostname'}
    # Add additional validation to ensure the host is a valid IP address or domain name
    try:
        subprocess.run(['ping', '-c', '1', host], check=True)
    except Exception as e:
        return {'error': str(e)}
    return {"status": "completed"}