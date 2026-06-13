from fastapi import FastAPI
import subprocess
def execute_command(command: str):
    parts = command.split()
    process = subprocess.Popen(parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if not host or len(host) > 255:
        return {"status": "failed", "error": "Invalid host"}
    command = f'ping -c 1 {host}'
    output, error = execute_command(command)
    if error:
        return {"status": "failed", "error": error.decode()}
    else:
        return {"status": "completed", "output": output.decode()}