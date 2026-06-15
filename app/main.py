from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.app = FastAPI()

    async def home(self):
        return {"message": "Agentic Self-Healing Pipeline"}

    async def ping(self, host: str):
        # Secure implementation
        if not PingService.is_valid_host(host):
            raise ValueError("Invalid host")
        args = ['ping', host]
        subprocess.run(args, check=True)

    @staticmethod
def is_valid_host(host: str) -> bool:
        allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
        return host in allowed_hosts

# Usage
glance_service = PingService()
glance_app = glance_service.app