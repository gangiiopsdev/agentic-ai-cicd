from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1']  # Define allowed hosts here

    async def ping(self, host: str) -> dict:
        if host not in self.allowed_hosts:
            return {'status': 'unauthorized'}
        # Validate the host input to ensure it does not contain malicious characters or patterns
        if not self.validate_host(host):
            return {'status': 'invalid_host'}
        command = ['ping', '-c', '4', host]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

    def validate_host(self, host: str) -> bool:
        # Add validation logic here, e.g., using regex to ensure the host is a valid IP address or hostname
        import re
        return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

app = FastAPI()
ping_service = PingService()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)