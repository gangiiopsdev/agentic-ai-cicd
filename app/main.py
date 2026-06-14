from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        # Secure implementation using subprocess.run with a list of arguments
        args = ['ping', '-c', '4', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation of the ping command
    if not host.isnumeric() and len(host) < 256:
        ping_command = PingCommand(host)
        status = ping_command.run()
        return {"status": status}
    else:
        return {"error": "Invalid host input"}