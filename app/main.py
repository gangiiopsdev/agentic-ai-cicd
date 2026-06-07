from fastapi import FastAPI
import subprocess
def execute_safe_command(command, *args):
    # Validate and sanitize input
    for arg in args:
        if not isinstance(arg, str) or not arg.isalnum():
            raise ValueError("Invalid argument")
    return subprocess.run([command] + list(args), capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError("Invalid input for ping command")
    result = execute_safe_command("ping", *host.split())  # Use safe splitting
    return {"status": "completed", "output": result.stdout}