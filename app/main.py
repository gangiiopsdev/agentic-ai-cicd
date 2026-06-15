from fastapi import FastAPI
import subprocess
import re
def validate_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}

    # Use a more secure method to avoid shell injection
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}