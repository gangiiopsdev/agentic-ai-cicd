from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_subprocess(command: list) -> str:
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return result.stdout.strip().split('\n')[-1]

def validate_host(host: str) -> bool:
    # More comprehensive regex to ensure the host is a valid domain or IP address
    pattern = r'^[a-zA-Z0-9-.:@,_]+(?:/[a-zA-Z0-9-.:@,_]*)*$'
    return re.match(pattern, host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host format")
    safe_host = shlex.quote(host)
    command = ['ping', '-c', '1', safe_host]
    output = subprocess.run(command, capture_output=True, text=True, check=False)
    return {"status": "completed", "output": output.stdout.strip() if output.stdout else ''}