from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate and sanitize the input before using it in subprocess
        if not self.host.isdigit():
            raise ValueError('Invalid input')
        try:
            subprocess.call(['ping', self.host])
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    result = command.execute()
    return {'status': result}