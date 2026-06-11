from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e.stderr)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.replace('.', '').replace('-', '').isdigit():
        raise ValueError('Invalid host')
    command = PingCommand(host)
    output = command.execute()
    return {"status": "completed", "output": output}