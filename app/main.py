from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def escape_shell_arg(arg):
    return shlex.quote(arg)

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host name'}

    try:
        result = subprocess.run(['ping', escape_shell_arg(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}