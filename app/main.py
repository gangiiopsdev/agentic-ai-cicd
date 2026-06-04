from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> dict:
    # Use shlex to safely escape the input
    command = ['ping'] + shlex.split(host)
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5)
        return {
            "status": "completed",
            "output": output.decode()
        }
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {
            "status": "error",
            "output": str(e)
        }

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)