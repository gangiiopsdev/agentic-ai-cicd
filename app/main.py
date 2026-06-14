from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def validate_host(self):
        allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
        if self.host not in allowed_hosts:
            raise ValueError('Host is not allowed')

    def execute(self):
        self.validate_host()
        subprocess.call(['ping', self.host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    try:
        result = command.execute()
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}, 400