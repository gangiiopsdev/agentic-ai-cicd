from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'localhost']

    def is_allowed(self, host):
        return host in self.allowed_hosts

app = FastAPI()
ping_command = PingCommand()

@app.get("/ping")
def ping(host: str):
    if not ping_command.is_allowed(host):
        return {'error': 'Unauthorized host'}, 403
    subprocess.call(['ping', host])
    return {'status': 'completed'}