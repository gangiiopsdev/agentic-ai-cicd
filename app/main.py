from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = allowed_hosts

    def ping(self, host):
        if host in self.allowed_hosts:
            subprocess.run(['ping', shlex.quote(host)], check=True)
        else:
            raise ValueError('Host not allowed')

app = FastAPI()
ping_service = SafePing(['example.com', 'another-example.com'])

@app.get('/ping')
def ping(host: str):
    try:
        ping_service.ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}