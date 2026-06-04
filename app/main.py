from fastapi import FastAPI
import subprocess
def execute_safe_command(command, *args):
    return subprocess.run([command] + list(args), capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if not host.isalnum():
        raise ValueError("Invalid input for ping command")
    result = execute_safe_command("ping", host)
    return {"status": "completed", "output": result.stdout}