from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout
class SafePing:
    def __init__(self, allow_all_hosts=False):
        self.allow_all_hosts = allow_all_hosts
        self.allowed_hosts = {'example.com'}

    def ping(self, host):
        if not self.allow_all_hosts and host not in self.allowed_hosts:
            raise ValueError('Unauthorized host')
        return safe_ping(host)
app = FastAPI()

@app.get('/ping')
def ping(host: str, safe_ping_instance=SafePing()):
    try:
        response = safe_ping_instance.ping(host)
        return {'status': 'completed', 'output': response}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}