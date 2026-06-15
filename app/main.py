from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.sanitized_commands = {
            "ping": True,
            # Add more safe commands as needed
        }

    def execute(self, command: str, *args, **kwargs):
        if command not in self.sanitized_commands:
            raise ValueError(f"Unsafe command detected: {command}")
        return subprocess.run([command] + list(args), capture_output=True, text=True, check=True)

app = FastAPI()
safe_ping = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to avoid command injection
    if not host.isalnum() or len(host) > 255:
        return {
            "status": "failed",
            "error": "Invalid hostname"
        }
    try:
        result = safe_ping.execute("ping", shlex.quote(host))
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e)
        }