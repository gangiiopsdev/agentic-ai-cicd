from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, command: str):
        self.command = command

    def execute(self):
        try:
            result = subprocess.run(self.command, shell=False, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(f"ping {host}")
    output = ping_command.execute()
    return {'status': 'completed', 'output': output}