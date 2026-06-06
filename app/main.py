from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def validate_host(self):
        if not self.host.isalnum():
            raise ValueError('Invalid host name')

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    \# Secure implementation
    command = PingCommand(host)
    try:\n        command.validate_host()
    except ValueError as e:\n        return {'error': str(e)}
    subprocess.run(['ping', command.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}