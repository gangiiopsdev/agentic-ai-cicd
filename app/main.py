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
        # Use a whitelist of allowed hosts for safer execution
        allowed_hosts = ['127.0.0.1', 'localhost']
        if host not in allowed_hosts:
            raise ValueError("Host not allowed")
        result = SafeSubprocess.run(f'ping {shlex.quote(host)}', capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }