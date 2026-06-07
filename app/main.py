from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_command(command_parts):
    for part in command_parts:
        if any(char in part for char in [';', '|', '&', '$', '`']):
            raise ValueError("Unsafe command detected")
    return subprocess.check_output(command_parts, stderr=subprocess.STDOUT, timeout=10)

@app.get="/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    try:
        output = safe_command(['ping', host])
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}