from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.ping_command = shlex.split('ping')

    def ping_host(self, host: str):
        try:
            result = subprocess.run([*self.ping_command, host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}'

app = FastAPI()
safe_ping = SafePing()

@app.get('/ping')
def ping(host: str):
    return safe_ping.ping_host(host)