from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation without shell=True
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            raise HTTPException(status_code=400, detail=f'Ping failed: {e.stderr}')


global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):  
    ping_command = PingCommand(host)
    return {'status': 'Pinging ' + host}