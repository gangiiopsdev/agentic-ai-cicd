from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    def ping(self, host: str):
        if host in self.allowed_hosts:
            # Use check_output to capture the output and handle errors safely
            try:
                result = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, text=True)
                return {'status': 'success', 'output': result}
            except subprocess.CalledProcessError as e:
                return {'status': 'failure', 'error': e.output}
        else:
            raise ValueError('Invalid host')

app = FastAPI()
safe_ping = SafePing()

@app.get('/ping')
def ping(host: str):
    return safe_ping.ping(host)