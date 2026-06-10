from fastapi import FastAPI
import subprocess
import shlex
class SafePinger:
    def __init__(self):
        self.ping_command = ['ping', '-c', '1']

    def ping(self, host: str):
        # Validate and sanitize the input to ensure it does not contain malicious content
        if not self.is_safe_host(host):
            raise ValueError('Invalid host name')
        command = self.ping_command + [shlex.quote(host)]
        return subprocess.run(command, capture_output=True, text=True)

    def is_safe_host(self, host: str) -> bool:
        # Implement a simple validation logic, e.g., check if the host contains only allowed characters
        return all(c.isalnum() or c in '.-' for c in host)

app = FastAPI()
safe_pinger = SafePinger()

@app.get("/ping")
def ping(host: str):
    result = safe_pinger.ping(host)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }