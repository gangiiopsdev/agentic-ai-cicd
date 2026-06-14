from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        if not isinstance(self.host, str) or not self.host.strip():
            raise ValueError('Invalid host provided')
        result = subprocess.run(['ping', self.host], check=True, capture_output=True, text=True)
        return result.stdout

        # Sanitize input to prevent shell injection
        import shlex
        safe_host = shlex.quote(self.host)

        result = subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
        return result.stdout
global ping_command
ping_command = PingCommand(None)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_command.host = host
    try:
        result = ping_command.run()
        return {'status': 'completed', 'output': result}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}