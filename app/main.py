from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', self.host], capture_output=True, text=True)
            return output.stdout
        except Exception as e:
            return str(e)

class PingEndpoint:
    @staticmethod
    def ping(host: str):,
        command = PingCommand(host)
        result = command.execute()
        return {'status': 'completed', 'result': result}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return PingEndpoint.ping(host)