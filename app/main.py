from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.command = 'ping'

    def safe_ping(self, host: str):
        args = [self.command] + shlex.split(host)
        subprocess.call(args, shell=False)  # Added shell=False to prevent command injection

global_safe_ping = SafePing().safe_ping
class PingRouter:
    @staticmethod
def ping(host: str):
        global_safe_ping(host)
        return {'status': 'completed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
ping_router = PingRouter()
app.add_api_route('/ping', ping_router.ping, methods=['GET'])