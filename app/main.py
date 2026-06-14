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

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host name")
    command = PingCommand(host)
    result = command.execute()
    return {"status": "completed", "result": result}

def validate_host(host):
    # Simple validation example, replace with actual validation logic
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts