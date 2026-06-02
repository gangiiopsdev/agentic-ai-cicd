from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

class PingCommand:
    def __init__(self, command: list):
        self.command = command

    def execute(self):
        try:
            result = subprocess.run(self.command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Command failed: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    ping_command = PingCommand(command)
    return ping_command.execute()