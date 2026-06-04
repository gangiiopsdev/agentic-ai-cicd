from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        if not validate_host(self.host):
            raise ValueError('Invalid host')
        subprocess.call(['ping', self.host], shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    try:
        command.run()
    except ValueError as e:
        return {'error': str(e)}
    return {"status": "completed"}