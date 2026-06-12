from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to prevent injection attacks
    if not PingCommand.is_valid_host(host):
        return {"status": "error", "result": "Invalid host"}
    result = PingCommand.safe_ping(host)
    return {"status": "completed", "result": result}

class HostValidator:
    @staticmethod
    def is_valid_host(hostname: str) -> bool:
        # Implement a whitelist of allowed hosts or use a regex pattern to validate the host
        allowed_hosts = ['127.0.0.1', 'localhost']  # Example whitelist
        return hostname in allowed_hosts