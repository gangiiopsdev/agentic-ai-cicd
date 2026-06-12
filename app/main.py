from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def execute_ping(host):
    try:
        # Validate host input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host name or IP address')
        # Use subprocess.run for safe execution
        result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = execute_ping(host)
    return {"status": "completed", "response": response}