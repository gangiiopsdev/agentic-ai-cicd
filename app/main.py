from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
global_args = ['ping']
cmd = global_args + [host]
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {"error": "Invalid host name"}
    command = PingCommand(host)
    output = command.execute()
    return {"status": "completed", "output": output}