from fastapi import FastAPI
import subprocess
import re
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Sanitize the host input to ensure it does not contain malicious characters
        if not re.match(r'^[a-zA-Z0-9-.]+$', self.host):
            raise ValueError('Invalid input')
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

app = FastAPI()

@app.get("/ping")
def ping(host: str):