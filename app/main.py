from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output = execute_command(command)
    return {"status": "completed", "output": output}
# Preventive controls:
# - Validate and sanitize the input to ensure it does not contain malicious content.
# - Use a whitelist of allowed hosts or commands.
# - Avoid using shell=True in subprocess calls unless absolutely necessary.