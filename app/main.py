from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return output.stdout.strip()
        except subprocess.CalledProcessError as e:
            return str(e)
class PingService:
    @staticmethod
def ping(host: str):
        # Sanitize input to prevent command injection
        if not host.isalnum():
            raise ValueError("Invalid characters in host")
        command = PingCommand(host)
        result = command.execute()
        return {'status': 'completed', 'result': result}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return PingService.ping(host)