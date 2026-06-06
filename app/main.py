from fastapi import FastAPI
import subprocess
import re
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await subprocess.run(['ping', self.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not self.is_valid_host(host):
        raise ValueError('Invalid host address')
    command = PingCommand(host)
    return await command.execute()

@staticmethod
async def is_valid_host(host: str) -> bool:
    # More robust validation for IPv4, IPv6, and hostname formats
    regex = re.compile(
        r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))' # IPv4
        r'|(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})' # IPv6
        r'|([a-zA-Z0-9]([-a-zA-Z0-9]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}' # hostname
    )
    return bool(regex.match(host))