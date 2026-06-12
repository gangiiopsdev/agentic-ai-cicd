from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

def validate_host(host):
    # Add validation logic here, e.g., allow only specific domains or IP addresses
    allowed_hosts = ['example.com', '127.0.0.1']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Host not allowed')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        command = PingCommand(host)
        output = command.execute()
        return {"status": "completed", "output": output}
    else:
        return {"error": "Invalid host"}