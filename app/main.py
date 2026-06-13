from fastapi import FastAPI
import subprocess
def run_safe_command(command: str, args: list):
    if not all(c.isalnum() for c in command):
        raise ValueError("Invalid command")
    return subprocess.call([command] + args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and safe command execution
    if not host.isalnum():
        return {"error": "Invalid input"}
    run_safe_command("ping", [host])
    return {"status": "completed"}