from fastapi import FastAPI
import subprocess

def run_safe_command(command: str):
    return subprocess.run(command.split(), capture_output=True, text=True, shell=False)

class SafePing:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        command = f'ping {self.host}'
        result = run_safe_command(command)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/"
async def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get="/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    return safe_ping.execute()