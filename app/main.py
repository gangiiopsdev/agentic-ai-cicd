from fastapi import FastAPI
import subprocess
from pydantic import validator
class Ping:
    def __init__(self):
        self.hosts = []

    async def add_host(self, host: str):
        if self._is_valid_host(host):
            self.hosts.append(host)

    @validator('host')
    def _is_valid_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual valid hosts
        if v not in allowed_hosts:
            raise ValueError('Invalid host')
        return v

app = FastAPI()
ping_service = Ping()

@app.get("/ping")
def ping(host: str):
    if host not in ping_service.hosts:
        return {"error": "Host not allowed"}

    # Secure implementation using subprocess.Popen
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}