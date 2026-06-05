from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', '{}']

    def run(self, host):
        args = [self.ping_command[0]].extend(self.ping_command[1].format(host).split())
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return output.stdout

app = FastAPI()
safe_ping_instance = SafePing()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    return safe_ping_instance.run(host)