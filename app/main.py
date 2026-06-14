from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}