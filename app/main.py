from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate and sanitize the input
        if not self.host or not isinstance(self.host, str) or ' ' in self.host:
            raise ValueError('Invalid input for ping command')
        command = ['ping', self.host]
        return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {"status": "completed", "output": result.stdout}