from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command_parts):
        try:
            subprocess.run(command_parts, check=True)
        except subprocess.CalledProcessError as e:
            return str(e), 500

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 64:
        return {"error": "Invalid host name"}, 400
    command_parts = shlex.split(f'ping -c 1 {shlex.quote(host)}')
    result, status = SafeSubprocess.run(command_parts)
    if status != 200:
        return {"error": result}, status
    return {"status": "completed", "details": result}