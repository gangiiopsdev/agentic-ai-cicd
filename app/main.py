from fastapi import FastAPI
import subprocess
from fastapi import HTTPException
import re

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation with shell=False and input validation
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            raise HTTPException(status_code=400, detail=f'Ping failed: {e.stderr}')


global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it's a valid hostname/IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail='Invalid host format')
    ping_command = PingCommand(host)
    return {"status": "Pinging " + host}