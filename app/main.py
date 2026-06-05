from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return subprocess.run(['ping', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Secure implementation
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {"status": "completed", "output": result.stdout}

def is_valid_host(host):
    # Add logic to validate the host
    allowed_hosts = ["example.com", "localhost"]
    return host in allowed_hosts