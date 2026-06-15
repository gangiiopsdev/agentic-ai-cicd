from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.allowed_hosts = ['google.com', 'example.com']  # Example allowed hosts

    def safe_ping(self, host: str):
        if host not in self.allowed_hosts:
            return {'status': 'error', 'message': 'Invalid host name'}
        command = shlex.split(f'ping {host}')
        subprocess.run(command, check=True)

app = FastAPI()
safe_ping_instance = SafePing()

@app.get('/ping')
def ping(host: str):
    return safe_ping_instance.safe_ping(host)