from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run with shell=False and proper input validation
        if not self.is_valid_host(self.host):
            raise ValueError("Invalid host")
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout

    def is_valid_host(self, host):
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
        return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService(host)
    return {'status': 'completed', 'output': service.execute()}