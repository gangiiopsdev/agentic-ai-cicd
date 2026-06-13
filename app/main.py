from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation
        command = ['ping', self.host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

global ping_command
ping_command = PingCommand('')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not self.is_safe_host(host):
        raise ValueError("Unsafe host detected")
    ping_command.host = host
    result = ping_command.execute()
    return {"status": "completed", "result": result}

@staticmethod
def is_safe_host(host: str) -> bool:
    # Implement your logic to check if the host is safe here
    allowed_hosts = ["example.com", "localhost"]
    return host in allowed_hosts