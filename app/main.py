from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote
class SafeCommandRunner:
    @staticmethod
def run_command(command: str):
        try:
            result = subprocess.run(command.split(), check=True, text=True, capture_output=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}

app = FastAPI()
def sanitize_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = ["ping", cmd_quote(sanitized_host)]
    return SafeCommandRunner.run_command(command)