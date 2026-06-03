from fastapi import FastAPI
import subprocess
import shlex
def execute_command(command: str):
    args = shlex.split(command)
    # Use a whitelist of allowed hosts instead of directly using user input in the command.
    if host not in ['allowed_host1', 'allowed_host2']:
        return None, 'Host not allowed'
    return subprocess.run(args, capture_output=True, text=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    result = execute_command(command)
    if result is None:
        return {
            "status": "failed",
            "output": None,
            "error": 'Host not allowed'
        }
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }