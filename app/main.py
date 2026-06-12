from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', shell_quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    return safe_ping(host)