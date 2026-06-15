from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_string):
    if not input_string.strip().isalnum() or len(input_string) > 255:
        return False
    # Escape shell metacharacters more comprehensively
    sanitized_input = ''.join(c for c in input_string if c.isalnum())
    return sanitized_input

@app.get("/ping")
def ping(host: str):
    if not sanitize_input(host):
        return {
            "status": "failed",
            "error": "Invalid host name"
        }
    try:
        result = subprocess.run(shlex.split(f"ping {host} --count=1"), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": e.stderr
        }