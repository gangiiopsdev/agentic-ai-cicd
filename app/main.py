from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.allowed_hosts = {'example.com', 'test.com'}  # Define a list of allowed hosts

    def safe_ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Invalid input')
        subprocess.call(['ping', shlex.quote(host)])  # Use shlex.quote to safely escape the host parameter
        return {'status': 'completed'}

app = FastAPI()
ping_handler = SafePing()

@app.get('/ping')
def ping(host: str):
    return ping_handler.safe_ping(host)