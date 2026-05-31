from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        command = shlex.split(command)
        return subprocess.run(command, capture_output=True, text=True, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.strip().isdigit():
            raise ValueError("Invalid host input")
        result = SafeSubprocess.run(f'ping {shlex.quote(host)}')
        return {
            "status": "completed",
            "output": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e)
        }
    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }