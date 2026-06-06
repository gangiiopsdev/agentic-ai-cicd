from fastapi import FastAPI
import subprocess
import shlex
class SafePinger:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']

    def safe_ping(self, host: str):
        if host in self.allowed_hosts:
            args = ['ping'] + shlex.split(host)
            return subprocess.call(args, shell=False)
        else:
            raise ValueError('Host not allowed')

app = FastAPI()
safe_pinger = SafePinger()

@app.get("/ping")
def ping(host: str):
    try:
        return {'status': 'completed', 'result': safe_pinger.safe_ping(host)}
    except ValueError as e:
        return {'error': str(e)}