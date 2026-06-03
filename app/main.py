from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def safe_ping(self):
        # Safe implementation using subprocess.Popen
        command = ['ping', self.host]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return output, error

def validate_host(host: str):
    # Simple validation to allow only alphanumeric characters and periods
    if not host.isalnum() and '.' not in host:
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get("/ping")
def ping(host: str):