from fastapi import FastAPI
import subprocess
import shlex
class HostValidator:
    def __init__(self, max_length=3):
        self.max_length = max_length

    def validate(self, host: str) -> bool:
        return host.isdigit() and len(host) <= self.max_length

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    validator = HostValidator()\n    if not validator.validate(host):\n        raise ValueError("Invalid host input")\n    command = ['ping', '-c', '1', shlex.quote(host)]\n    result = subprocess.run(command, check=True, capture_output=True, text=True)\n    return {"status": "completed", "output": result.stdout}