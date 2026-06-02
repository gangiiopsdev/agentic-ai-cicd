from fastapi import FastAPI
import subprocess
import shlex

class InputSanitizer:
    @staticmethod
def sanitize_host(host):
        return ''.join(c for c in host if c.isalnum())

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Use Pydantic model to validate input
    sanitized_host = InputSanitizer.sanitize_host(host)
    if not sanitized_host:
        raise ValueError("Invalid input")
    command = shlex.split(f'ping {shlex.quote(sanitized_host)}')
    subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed"}