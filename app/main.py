from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Sanitize the host input before using it in the command
        if not is_valid_host(self.host):
            raise Exception("Invalid host")
        return subprocess.run(['ping', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = command.execute()
    return {"status": "completed", "output": result.stdout}

def is_valid_host(host: str) -> bool:
    # Add your validation logic here
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        return True
    return False