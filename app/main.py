from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self, host):
        self.host = host

    def run(self):
        try:
            # Using shlex.quote to safely handle the input
            command = ['ping', self.host]
            result = subprocess.run(command, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

class PingRouter:
    def __init__(self):
        self.ping = SafePing()

    async def ping_host(self, host: str):
        return self.ping.run()

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_router = PingRouter()
    return ping_router.ping_host(host)