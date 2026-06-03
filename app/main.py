from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', subprocess.quote(self.host)], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
class PingEndpoint:
    @staticmethod
def home():
        return {"message": "Agentic Self-Healing Pipeline"}

    @staticmethod
def ping(host: str):
        command = PingCommand(host)
        return {"status": command.execute()}

app = FastAPI()

@app.get("")
def home():
    return PingEndpoint.home()

@app.get("/ping")
def ping(host: str):
    return PingEndpoint.ping(host)