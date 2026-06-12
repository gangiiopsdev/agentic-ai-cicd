from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, command: str):
        self.command = command

    def execute(self):
        try:
            result = subprocess.run(self.command.split(), check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 64:
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        ping_command = PingCommand(f'ping -c 1 {host}')
        result = ping_command.execute()
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}