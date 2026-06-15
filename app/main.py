from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate and sanitize the host input
        if not all(c.isalnum() or c in ['.', '-'] for c in self.host):
            raise ValueError('Invalid host name')
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return {'status': 'completed', 'output': command.execute()}}