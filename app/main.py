from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Safe implementation using list instead of shell command
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
class PingRouter:
    def __init__(self):
        self.ping_service = PingService()

    @app.get("/ping")
def ping(host: str):\n        result = self.ping_service.ping(host)\n        return {"status": "completed", "result": result}

app = FastAPI()\napp.add_route(", "/ping", PingRouter().ping)