from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except Exception as e:
            return {"status": "error", "message": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host before using it
    if validate_host(host):
        ping_command = PingCommand(host)
        return ping_command.execute()