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
        if not host.strip().isdigit() or int(host) < 0 or int(host) > 255:
            raise ValueError("Invalid host input")
        result = SafeSubprocess.run(f'ping -c 1 {shlex.quote(host)}', capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

# Preventive controls
1. Ensure that the host input is validated and sanitized before being used in subprocess commands.
2. Use a whitelist of allowed hosts instead of allowing any IP address.
3. Consider using parameterized queries or a safe API for network operations to avoid shell injection attacks.