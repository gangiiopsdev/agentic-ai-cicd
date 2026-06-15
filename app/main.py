from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ['ping', self.host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host detected")
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {"status": "completed", "result": result}

@staticmethod
def is_safe_host(host: str) -> bool:
    allowed_hosts = ["example.com", "localhost"]
    return host in allowed_hosts