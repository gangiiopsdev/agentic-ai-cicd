from fastapi import FastAPI, HTTPException
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run with shell=False and safe arguments
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand()

    @app.get("/ping")
    def ping(self, host: str):
        # Validate the host parameter to ensure it is a valid IP address or hostname
        if not self.validate_host(host):
            raise HTTPException(status_code=400, detail="Invalid host")
        return {"status": "completed", "result": self.ping_command.execute()}

def validate_host(host: str) -> bool:
    import re
    # Regular expression to match a valid IP address or hostname
    pattern = re.compile(r'^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|[a-zA-Z0-9.-]+)$')
    return bool(pattern.match(host))

app = FastAPI()
ping_endpoint = PingEndpoint()