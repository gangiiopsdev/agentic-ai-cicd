from fastapi import FastAPI
import subprocess
import shlex
global MAX_PINGS
MAX_PINGS = 4
def safe_ping(host):
    command = f'ping -c {MAX_PINGS} '  # Use a global variable for the number of pings
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