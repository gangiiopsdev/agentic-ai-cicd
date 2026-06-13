from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Validate input to prevent command injection
        if not all(c.isalnum() or c in '.-' for c in host):
            return "Invalid host"
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
global app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return PingService.ping(host)