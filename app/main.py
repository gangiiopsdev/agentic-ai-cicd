from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        self.hosts = []

    async def add_host(self, host: str):
        if self._is_valid_host(host):
            self.hosts.append(host)

    def _is_valid_host(self, host: str):
        # Add logic to validate the host input
        return True

app = FastAPI()
ping_service = Ping()

@app.get("/ping")
def ping(host: str):
    if host not in ping_service.hosts:
        return {"error": "Host not allowed"}

    # Secure implementation using subprocess.run with input validation
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}