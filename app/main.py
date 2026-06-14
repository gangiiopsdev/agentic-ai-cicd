from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def is_valid_host(self):
        # Implement host validation logic here (e.g., allow only certain IPs)
        return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if PingCommand(host).is_valid_host():
        subprocess.call(['ping', '-c', '1', f'{self.host}'])  # Use -c to limit the number of pings
    else:
        return {'status': 'Invalid host'}
    return {'status': 'completed'}