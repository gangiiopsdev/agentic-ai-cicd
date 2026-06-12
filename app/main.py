from fastapi import FastAPI
import subprocess
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
    # Validate the host to prevent command injection
    if not PingCommand.is_valid_host(host):
        raise ValueError("Invalid host")
    result = PingCommand.safe_ping(host)
    return {"status": "completed", "result": result}

class PingCommand:
    @staticmethod
def is_valid_host(host: str) -> bool:
        # Simple validation to allow only alphanumeric characters and hyphens
        return all(c.isalnum() or c == '-' for c in host)