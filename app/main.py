from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation without shell=True
        subprocess.run(['ping', self.host], capture_output=True, text=True)


global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):  
    ping_command = PingCommand(host)
    return {'status': 'Pinging ' + host}