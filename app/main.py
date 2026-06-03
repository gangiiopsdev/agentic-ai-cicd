from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it does not contain malicious content
    if not host.isalnum() or '.' not in host:
        return {"error": "Invalid host parameter"}, 400
    command = PingCommand(host)
    result = command.execute()
    return {"status": "completed", "output": result.stdout}