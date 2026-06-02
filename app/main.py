from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command_parts):
        cmd = subprocess.Popen(command_parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        return output, error
class PingRouter:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str):
        try:
            command_parts = shlex.split(f"ping {host}")
            output, error = SafeSubprocess.call(command_parts)
            return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}
        except Exception as e:
            return {"status": "failed", "error": str(e)}
PingRouter()