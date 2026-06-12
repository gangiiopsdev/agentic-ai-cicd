from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    def __init__(self):
        self.allowed_hosts = set(['192.168.0.1', '192.168.0.2'])

    def secure_ping(self, host: str):
        if host not in self.allowed_hosts:
            return {'status': 'invalid_host'}
        ping_command = ['ping', shlex.quote(host)]
        try:
            subprocess.run(ping_command, shell=False, check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.secure_ping(host)