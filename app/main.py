from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand()

    @app.get("/ping")
    def ping(self, host: str):\n        try:\n            result = self.ping_command.execute()
            return {"status": "completed", "result": result}\n        except Exception as e:\n            return {"status": "error", "message": str(e)}