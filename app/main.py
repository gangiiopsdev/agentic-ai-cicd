from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_commands = {'ping': True}

    def safe_subprocess_run(self, command, host):
        if command in self.safe_commands:
            return subprocess.run([command, host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        else:
            raise ValueError('Unsafe command')

global_safe_ping = SafePing()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = global_safe_ping.safe_subprocess_run('ping', host)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"error": str(e)}