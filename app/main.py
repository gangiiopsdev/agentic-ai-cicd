from fastapi import FastAPI, HTTPException
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ['ping', self.host]
        # Validate or sanitize the input to prevent command injection
        if not self.is_valid_host(self.host):
            raise HTTPException(status_code=400, detail='Invalid host')
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    def is_valid_host(self, host):
        # Implement validation logic here (e.g., regex check)
        return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):