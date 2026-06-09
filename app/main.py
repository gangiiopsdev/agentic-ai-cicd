from fastapi import FastAPI
import shlex
import subprocess
class SafePing:
    def __init__(self):
        pass

    def safe_ping(self, host: str) -> dict:
        if not self.is_safe_host(host):
            return {'status': 'error', 'message': 'Invalid host'}
        try:
            args = ['ping'] + shlex.split(host)
            result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
            return {'status': 'success', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

    def is_safe_host(self, host: str) -> bool:
        # Add logic to validate the host here
        allowed_hosts = ['example.com', 'localhost']
        return host in allowed_hosts

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping_endpoint(host: str):
    if safe_ping_instance.is_safe_host(host):
        return safe_ping_instance.safe_ping(host)
    else:
        return {'status': 'error', 'message': 'Invalid host'}