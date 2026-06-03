from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_command(command: str) -> list:
    return shlex.split(command)

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to ensure it is a safe hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError("Invalid host")
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}