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

app = FastAPI()
def escape_host(host: str):
    return ''.join(ch for ch in host if ch.isalnum() or ch.isspace())

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    command = f"ping {escaped_host}"
    result = SafeSubprocess.safe_call(command)
    return {"status": "completed", "result": result}