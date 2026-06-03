from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        # Use a whitelist of allowed hosts or use a more secure method to construct the command
        allowed_hosts = ['example.com', 'test.com']
        if self.host in allowed_hosts:
            subprocess.run(['ping', self.host], check=True)
        else:
            raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    try:
        command.execute()
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 400