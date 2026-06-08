from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']

    async def safe_ping(self, host: str):
        if host in self.allowed_hosts:
            command = shlex.split(f'ping -c 4 {host}')
            result = subprocess.run(command, capture_output=True, text=True, check=False)
            return result.stdout
        else:
            raise ValueError('Invalid host')

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    output = safe_ping_instance.safe_ping(host)
    return {'status': 'completed', 'output': output}