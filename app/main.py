from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        args = ['ping', '-c', '1', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

class PingEndpoint:
    def __init__(self):
        pass

    @staticmethod
    def ping(host: str):
        try:
            ping_command = PingCommand(host)
            response = ping_command.run()
            return {'status': 'completed', 'output': response}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return PingEndpoint.ping(host)