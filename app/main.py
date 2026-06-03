from fastapi import FastAPI
import subprocess
from shlex import quote
def ping(host: str):
    try:
        # Use os.path.abspath to ensure the command is executed with an absolute path
        result = subprocess.run(['ping', '-c', '1', os.path.abspath(host)], capture_output=True, text=True, check=True)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)