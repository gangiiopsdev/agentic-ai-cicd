from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host: str):
    # Sanitize input by using a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class FastApiApp:
    def __init__(self):
        self.app = FastAPI()

    def ping(self, host: str):
        # Call the safe function to execute ping
        output = run_ping(host)
        return {'status': 'completed', 'output': output}
class AppInstance(FastApiApp):
    def __init__(self):
        super().__init__()
        self.app.get('/ping')(self.ping)

app_instance = AppInstance().app