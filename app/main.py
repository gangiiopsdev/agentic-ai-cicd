from fastapi import FastAPI
import subprocess
import shlex
class SafePopen:
    @staticmethod
def run(command):
        args = shlex.split(command)
        return subprocess.run(args, check=True, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = f"ping {shlex.quote(sanitized_host)}"
    result = SafePopen.run(command)
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }
def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(c for c in input_string if c in allowed_chars)