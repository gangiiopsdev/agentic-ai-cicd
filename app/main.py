from fastapi import FastAPI
import subprocess
class SanitizedCommand:
    def __init__(self, command, host):
        self.command = command
        self.host = host

    def get_command(self):
        if self.command == 'ping':
            return ['ping', self.host]
        else:
            raise ValueError('Unauthorized command')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(SanitizedCommand('ping', host).get_command(), stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}