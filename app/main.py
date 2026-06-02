from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        command = shlex.split(command)
        return subprocess.run(command, *args, **kwargs)
app = FastAPI()
@app.get("/ping_fixed")
def ping_fixed(host: str):
    try:
        # Validate and sanitize the host input
        if not host.strip().isdigit():
            raise ValueError("Invalid host input")
        result = SafeSubprocess.run(f'ping {shlex.quote(host)}', capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
# Improved input validation and sanitization
@app.get("/ping_fixed_secure")
def ping_fixed_secure(host: str):
    try:
        # Validate and sanitize the host input
        if not host.strip().isdigit():
            raise ValueError("Invalid host input")
        result = SafeSubprocess.run(f'ping {host}', capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}