from fastapi import FastAPI
import subprocess
import re
def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9]{1,255}$', host) is not None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}

    args = ['ping', re.escape(host)]  # Use re.escape to escape special characters in the hostname
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}