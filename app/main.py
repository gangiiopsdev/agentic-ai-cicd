from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        try:
            output = subprocess.check_output(['ping', self.host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not host or len(host) > 255 or not all(c.isalnum() or c in '.-_' for c in host):
        return {'status': 'error', 'output': 'Invalid host'}
    ping_command = PingCommand(host)
    return ping_command.run()

# Add additional security measures to further harden the application

import os
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)