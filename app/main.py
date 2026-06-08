from fastapi import FastAPI
import subprocess
def run_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        raise ValueError("Invalid input")
    command_parts = ["ping", host]
    output = run_command(command_parts)
    return {"status": "completed", "output": output}