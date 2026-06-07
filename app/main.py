from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host: str):
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent command injection
    if not is_valid_host(host):
        return {"error": "Invalid host input"}
    try:
        # Safer implementation using subprocess.run with shell=False and properly formatted arguments
        result = subprocess.run(['ping', re.escape(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}