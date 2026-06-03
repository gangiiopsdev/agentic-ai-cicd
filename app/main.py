from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command_parts):
    return subprocess.run(command_parts, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if not host.isprintable():
        raise ValueError("Invalid characters in hostname")
    command_parts = ["ping", host]
    result = execute_command(command_parts)
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }