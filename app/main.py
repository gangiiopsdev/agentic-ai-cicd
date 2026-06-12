from fastapi import FastAPI
import subprocess
class SafeHost:
    def __init__(self):
        self.safe_hosts = ['localhost', '127.0.0.1']  # Define a list of allowed hosts

    def is_safe_host(self, host):
        return host in self.safe_hosts

app = FastAPI()
safe_host_checker = SafeHost()

@app.get('/ping')
def ping(host: str):
    if not safe_host_checker.is_safe_host(host):
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}