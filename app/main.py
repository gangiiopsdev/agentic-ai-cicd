from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        # Secure implementation using subprocess.Popen
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

global ping_command
ping_command = PingCommand(None)

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_command
    ping_command.host = host
    output = ping_command.run()
    return {"status": "completed", "output": output}