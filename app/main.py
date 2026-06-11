from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def validate_host(host):
    if not host.isalnum():
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"error": "Invalid input"}
    args = ['ping', quote(host)]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}