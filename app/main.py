from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        allowed_hosts = ['example.com', 'test.com']
        if self.host not in allowed_hosts:
            raise ValueError('Invalid host')
        subprocess.run(['ping', self.host], check=True)

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    try:
        command.execute()
    except ValueError as e:
        return {'error': str(e)}
    return {'status': 'completed'}