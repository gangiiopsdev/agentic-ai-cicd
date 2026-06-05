from fastapi import FastAPI
import subprocess
class SafePinger:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']

    def safe_ping(self, host: str):
        if host in self.allowed_hosts:
            args = ['ping', '-c', '1', subprocess.check_output(['echo', host], text=True).strip()]
            return subprocess.call(args)
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