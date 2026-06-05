from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        if not self.is_valid_host(host):
            return 'Invalid host'
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error: {e}

    def is_valid_host(self, host: str) -> bool:
        import re
        pattern = r'^[a-zA-Z0-9.-]+$'
        return re.match(pattern, host) is not None

global_ping_service = PingService()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return global_ping_service.ping(host)