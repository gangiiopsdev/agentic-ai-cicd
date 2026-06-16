from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        # Safe implementation using a list of arguments and validating input
        if isinstance(self.host, str) and all(c.isalnum() or c in ' .-/' for c in self.host):  # Basic validation
            subprocess.run(['ping', self.host], check=True)
        else:
            raise ValueError('Invalid host input')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    ping_command.execute()
    return {"status": "completed"}