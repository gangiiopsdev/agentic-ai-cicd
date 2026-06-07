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
        if not host.strip() or ' ' in host:
            raise ValueError("Invalid host input")
        result = SafeSubprocess.run(f'ping -c 1 {host}', capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }