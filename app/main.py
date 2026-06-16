from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        command = ['ping', self.host]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
global_ping_command = PingCommand('example.com')
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or '.' not in host:
        return {'status': 'error', 'message': 'Invalid host input'}
    try:
        result = global_ping_command.run()
        return {'status': 'completed', **result}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}