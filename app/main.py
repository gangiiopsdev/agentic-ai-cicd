from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safer implementation using list for arguments
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    try:
        ping_command.execute()
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}