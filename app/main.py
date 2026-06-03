from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    return subprocess.run(['ping', host], capture_output=True, text=True)

def safe_execute_command(command_parts):
    if any(part in command_parts for part in ['&&', ';', '|']):
        raise ValueError('Unsafe command detected')
    return subprocess.run(command_parts, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = safe_execute_command(['ping', host])
    return {
        "status": "completed",
        "output": result.stdout,
        "stderr": result.stderr
    }