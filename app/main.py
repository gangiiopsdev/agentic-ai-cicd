from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    command = 'ping -c 4 '  # Add a default number of pings for security
    args = shlex.split(command + host)
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }

def ping(host: str):
    try:
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "stdout": e.stdout,
            "stderr": e.stderr,
            "returncode": e.returncode
        }