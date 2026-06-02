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
        if not host.strip().isdigit() or len(host) > 15:
            raise ValueError("Invalid host input")
        allowed_hosts = ['127.0.0.1', 'localhost']
        if host not in allowed_hosts:
            raise ValueError("Host not allowed")
        # Validate and sanitize other command-line arguments
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