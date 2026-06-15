from fastapi import FastAPI
import subprocess
import shlex
class SafePinger:
    def __init__(self):
        self.allowed_hosts = {'example.com', 'test.com'}

    async def ping(self, host: str):
        if host not in self.allowed_hosts:
            return {'status': 'error', 'output': 'Host is not allowed to be pinged.'}
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': str(e)}

app = FastAPI()
pinger = SafePinger()

@app.get("/ping")
def ping(host: str):
    return pinger.ping(host)