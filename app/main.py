from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Using subprocess.run instead of subprocess.call for security reasons
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        ping_command = PingCommand(host)
        return ping_command.execute()
    else:
        return {'status': 'error', 'output': 'Invalid host'}