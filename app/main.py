from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Secure implementation with validation and sanitization
    if not host or ' ' in host:
        return False, "Invalid input"
    try:
        output = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return True, output.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

def ping(host: str):
    success, result = secure_ping(host)
    if not success:
        return {"status": "failed", "error": result}
    else:
        return {"status": "completed", "output": result}