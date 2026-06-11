from fastapi import FastAPI
import shlex
import subprocess
global app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid injection attacks
    args = ['ping', '-c', '4', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}