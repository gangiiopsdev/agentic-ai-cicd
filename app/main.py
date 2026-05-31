from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        command = shlex.split(command)
        return subprocess.run(command, *args, **kwargs)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.strip().isdigit() or len(host) > 3:
            raise ValueError("Invalid host input")
        # Use subprocess.run safely with shell=False to avoid command injection
        result = SafeSubprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }