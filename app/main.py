from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_call(command: str):
        try:
            result = subprocess.run(shlex.split(command), check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

def escape_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    escaped_host = ''.join(ch for ch in host if ch in allowed_chars)
    return escaped_host

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    command = f"ping {escaped_host}"
    result = SafeSubprocess.safe_call(command)
    return {"status": "completed", "result": result}