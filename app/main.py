from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __call__(self, host):
        if self.is_valid_host(host):
            ping_command = ['ping'] + shlex.split(host)
            return subprocess.run(ping_command, capture_output=True, text=True)
        else:
            raise ValueError("Invalid host")

    def is_valid_host(self, host):
        # Simple validation to ensure the input does not contain shell metacharacters
        return all(c.isalnum() or c in ('.', '-') for c in host)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}