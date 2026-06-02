from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        subprocess.call(['ping', self.host.strip()], shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    if validate_host(host):
        ping_command.execute()
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., checking for allowed host patterns
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None