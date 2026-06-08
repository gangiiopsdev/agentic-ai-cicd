from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

def validate_host(host):
    allowed_hosts = ['example.com']  # Add your allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = PingCommand(host)
    return {'status': 'completed', 'output': command.execute()}