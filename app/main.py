from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def secure_ping(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize user input
    if not self.is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    ping_command = PingCommand(host)
    return ping_command.secure_ping()

    def is_valid_host(self, host):
        # Implement validation logic here
        allowed_hosts = ['127.0.0.1', 'localhost']
        return host in allowed_hosts