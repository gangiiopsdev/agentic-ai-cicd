from fastapi import FastAPI
import subprocess

def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid input')
    command_parts = ["ping", host]
    output = execute_safe_command(command_parts)
    return {"status": "completed", "output": output}