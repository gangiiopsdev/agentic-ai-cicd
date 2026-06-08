from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):  # Basic validation of input
        return "Invalid input"
    command = ['ping', '-c', '1', host]  # Use list to avoid shell=True
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return {"status": "success", "output": result.stdout}
    else:
        return {"status": "failure", "error": result.stderr}

def safe_ping_with_shell(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):  # Basic validation of input
        return "Invalid input"
    command = shlex.split(f'ping -c 1 {host}')  # Use shlex to safely split the command
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return {"status": "success", "output": result.stdout}
    else:
        return {"status": "failure", "error": result.stderr}

@app.get("/ping")
def ping(host: str):
    result = safe_ping_with_shell(host)
    if isinstance(result, dict) and 'status' in result:
        return result
    else:
        return {"message": result}