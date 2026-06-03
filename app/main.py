from fastapi import FastAPI
import shlex
import subprocess

class SafePing:
    def __init__(self):
        self.hosts = set()

    async def add_host(self, host: str):
        if host not in self.hosts:
            self.hosts.add(host)
            await self.ping_host(host)

    async def ping_host(self, host: str):
        args = shlex.split(f'ping -c 4 {host}')
        try:
            output = subprocess.run(args, capture_output=True, text=True, check=True)
            print(output.stdout)
        except subprocess.CalledProcessError as e:
            print(str(e))

app = FastAPI()
safe_ping_instance = SafePing()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    safe_ping_instance.add_host(host)
    return {"status": "completed", "result": "Ping initiated for host: {}".format(host)}