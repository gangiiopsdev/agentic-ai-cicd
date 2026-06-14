from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, command):
        self.command = command.strip()

    def execute(self):
        args = self.command.split()
        return subprocess.run(args, check=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host.strip() != 'localhost' and host.strip() != '127.0.0.1':
        raise ValueError('Invalid host')
    command = f"ping {host}"
    ping_instance = PingCommand(command)
    result = ping_instance.execute()
    return {"status": "completed", "output": result}