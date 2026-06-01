from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        # Fixed implementation using subprocess.run with shell=False and a safe argument list
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    try:
        ping_command.execute()
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}