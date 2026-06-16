from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent command injection
    if not all(c.isalnum() or c in ".-" for c in host):
        return {'status': 'error', 'message': 'Invalid host'}

    # Use subprocess.run with shell=False and properly sanitized arguments
    result = subprocess.run(['ping'] + shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}