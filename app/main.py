from fastapi import FastAPI
import subprocess
import shlex

def is_valid_host(host: str) -> bool:
    # Basic validation to ensure the host parameter is safe
    return all(c.isalnum() or c in '.-_' for c in host)

def validate_command(command: list) -> None:
    # Validate command components
    for component in command:
        if not isinstance(component, str):
            raise ValueError("Invalid command component")

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host parameter"}
    command = ["ping", shlex.quote(host)]
    validate_command(command)
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    return {"status": "completed", "output": output.decode()}