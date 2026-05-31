from fastapi import FastAPI
import subprocess
from sanic.response import text

app = FastAPI()

def safe_ping(host: str) -> dict:
    # Validate and sanitize input further if necessary
    return {'status': 'completed', 'output': ''}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return text('Invalid input', status=400)
    try:
        args = ['ping', '-c', '1', host]  # Limit the number of pings for security
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}