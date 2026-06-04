from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, max_pings: int = 5):
        self.max_pings = max_pings

    def ping(self, host: str):
        if not self.is_valid_host(host):
            raise ValueError("Invalid host")
        args = ['ping', '-c', str(self.max_pings), host]
        return subprocess.run(args, capture_output=True, text=True)

    def is_valid_host(self, host: str) -> bool:
        allowed_hosts = ['example.com', 'localhost']  # Replace with actual validation logic
        return host in allowed_hosts

class PingRouter:
    def __init__(self):
        self.safe_ping = SafePing()

    @app.get("/ping")
    def ping(self, host: str):
        result = self.safe_ping.ping(host)
        return {
            "status": "completed",
            "stdout": result.stdout,
            "stderr": result.stderr
        }

app = FastAPI()
ping_router = PingRouter()