from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def execute_ping(host):
    # Regex to validate IP addresses and localhost
    ip_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
    if re.match(ip_pattern, host) or host == 'localhost':
        try:
            output = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
    else:
        return "Invalid host"

@app.get("/ping")
def ping(host: str):
    result = execute_ping(host)
    return {"status": "completed", "output": result}