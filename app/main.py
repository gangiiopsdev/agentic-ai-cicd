from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', '-c', '4', self.host], stderr=subprocess.STDOUT)
            return output.decode()
        except subprocess.CalledProcessError as e:
            return e.output.decode()
class PingRouter:
    def __init__(self):
        self.ping_command = PingCommand('host')

    async def ping(self, host: str):
        if not self.is_valid_host(host):  # Simple validation to avoid injection
            return {'error': 'Invalid input'}
        result = self.ping_command.execute()
        return {'status': 'completed', 'result': result}

    def is_valid_host(self, host):
        allowed_hosts = ['192.168.1.1', '10.0.0.1']  # Add more allowed hosts as needed
        return host in allowed_hosts

app = FastAPI()
ping_router = PingRouter()

@app.get("/ping")
def ping(host: str):
    return ping_router.ping(host)