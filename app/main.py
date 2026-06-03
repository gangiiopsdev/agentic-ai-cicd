from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    return host.isalnum() and ' ' not in host

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        args = ['ping', shlex.quote(self.host)]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}

def validate_host(host: str) -> bool:
    return host.isalnum() and ' ' not in host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline" }

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        command = PingCommand(host)
        return command.execute()
    else:
        return {"status": "failed", "error": "Invalid input"}