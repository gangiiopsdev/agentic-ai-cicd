from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):  # Add validation for host input
    if not host.isalnum():  # Simple example of validation
        return {"status": "error", "message": "Invalid host input"}
    command = shlex.split(f"ping {host}")
    output = execute_command(command)
    return {"status": "completed", "output": output}