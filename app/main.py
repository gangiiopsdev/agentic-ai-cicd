from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    def __init__(self):
        self.host_list = ['8.8.8.8', '1.1.1.1']

    async def ping(self, host: str):
        if host not in self.host_list:
            return "Invalid input"
        command = shlex.split(f'ping {host}')
        subprocess.call(command)

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)