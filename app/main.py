from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def run(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
class PingRouter:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
def ping(host: str):  # Vulnerable implementation
        return PingCommand.run(host)

ping_router = PingRouter().app