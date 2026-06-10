from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_call(command: str):
        try:
            result = subprocess.run(shlex.split(command), shell=False, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

def escape_host(host: str):
    return ''.join(ch for ch in host if ch.isalnum() or ch.isspace())

def validate_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_ '
    return all(char in allowed_chars for char in host)

app = FastAPI()
@app.get("/ping")
def ping(host: str):  # Input validation added
    if not validate_host(host):
        return {"status": "error", "message": "Invalid input"}
    escaped_host = escape_host(host)
    command = f"ping -c 1 {escaped_host}"  # Limiting the number of pings to prevent DoS
    result = SafeSubprocess.safe_call(command)
    return {"status": "completed", "result": result}