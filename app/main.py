from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def call(host: str):
        # Validate and sanitize the host input
        if not PingCommand.is_valid_host(host):
            raise ValueError("Invalid host")
        return subprocess.run(['ping', '--', host], capture_output=True, text=True)

    @staticmethod
def is_valid_host(host: str) -> bool:
        import re
        # Simple regex to validate a hostname or IP address
        pattern = r'^[a-zA-Z0-9.-]+$'
        return re.match(pattern, host) is not None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input using shlex.quote to prevent shell injection
    import shlex
    safe_host = shlex.quote(host)
    result = PingCommand.call(safe_host)
    return {"status": "completed", "output": result.stdout}