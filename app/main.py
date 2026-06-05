from fastapi import FastAPI
import subprocess
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

@app.get(")
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
    try:
        # Check if the host is a valid IPv4 address or hostname
        import socket
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False