from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Regular expression for valid hostnames and IP addresses
valid_host_pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
def execute_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1', subprocess.check_output(['nslookup', host], text=True).strip().splitlines()[-1]], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
@app.get("/ping")
def ping(host: str):
    if not valid_host_pattern.match(host):
        return {"status": "error", "result": "Invalid host"}
    result = execute_ping(host)
    return {"status": "completed", "result": result}