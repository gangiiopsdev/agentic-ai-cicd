from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        try:
            args = shlex.split(f"ping {host}")
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": str(e)}

ping_command = PingCommand()