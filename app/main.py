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
def ping(host: str):  # Validate input more strictly
    validator = HostValidator()
    if not validator.validate(host):
        raise ValueError("Invalid host input")
    command = ['ping', '-c', '1'] + [shlex.quote(host)]  # Use shlex.quote to escape command arguments
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}