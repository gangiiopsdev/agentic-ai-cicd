from fastapi import FastAPI
import subprocess
def run_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before using it in the command
    if not host.isalnum():
        raise ValueError("Invalid host name")
    sanitized_host = subprocess.list2cmdline([host])
    command = ["ping", sanitized_host]
    output = run_command(command)
    return {"status": "completed", "output": output}