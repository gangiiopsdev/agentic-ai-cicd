from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', '-c', '4', self.host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not PingUtils.is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    ping_command = PingCommand(host)
    return ping_command.execute()
class PingUtils:
    @staticmethod
    def is_safe_host(host):
        # Implement a whitelist of allowed hosts here
        safe_hosts = ['127.0.0.1', 'localhost']
        return host in safe_hosts