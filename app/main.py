from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        # Sanitize the host input before using it in the subprocess command
        if not all(c.isalnum() or c.isdigit() or c in ('.', '-', '_') for c in self.host):
            raise ValueError('Invalid characters in host input')
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    command.run()
    return {'status': 'completed'}