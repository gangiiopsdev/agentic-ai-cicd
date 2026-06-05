from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host
        self.allowed_hosts = ['127.0.0.1', '::1']

    def is_safe_host(self):
        return self.host in self.allowed_hosts

    def run_command(self):
        if self.is_safe_host():
            try:
                result = subprocess.run(['ping', self.host], capture_output=True, text=True)
                return {'status': 'completed', 'output': result.stdout}
            except Exception as e:
                return {'status': 'failed', 'error': str(e)}
        else:
            return {'status': 'failed', 'error': 'Unsafe host'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.run_command()