from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def run(self) -> None:
        # Fixed implementation using subprocess.run for better security and error handling
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        print(result.stdout)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use PingCommand class to encapsulate the logic and improve security
    command = PingCommand(host)
    command.run()
    return {'status': 'completed'}