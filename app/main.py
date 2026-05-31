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
        if not host.strip().isdigit():
            raise ValueError("Invalid host input")
        # Use a whitelist of allowed hosts instead of validating digits only
        allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example list, update with actual allowed IPs
        if host not in allowed_hosts:
            raise ValueError("Invalid host input")
        result = SafeSubprocess.run(f'ping {host}', capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}