from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        try:
            subprocess.run(['ping', self.host], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Ping failed with error: {e}')

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    command = PingCommand(host)
    command.execute()
    return {"status": "completed"}