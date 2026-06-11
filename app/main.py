from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_safe_command(command: str) -> bool:
    return command.replace(' ', '').isalnum() and len(command.strip()) == len(re.sub(r'[a-zA-Z0-9]+', '', command)) == 0

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not is_safe_command(host) or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")

    # Secure implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}