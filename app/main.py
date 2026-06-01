from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1']  # Define allowed hosts here

    async def ping(self, host: str) -> dict:
        if host not in self.allowed_hosts or not self.is_safe_host(host):
            return {'status': 'unauthorized'}
        command = ['ping', '-c', '4', host]
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

    def is_safe_host(self, host: str) -> bool:
        # Implement a more robust validation logic here
        return self.is_ip_address(host)

    @staticmethod
def is_ip_address(ip: str) -> bool:
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or int(part) < 0 or int(part) > 255:
                return False
        return True

app = FastAPI()
ping_service = PingService()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)