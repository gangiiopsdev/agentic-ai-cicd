from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _execute_command(command_parts):
    try:
        output = subprocess.check_output(command_parts, stderr=subprocess.STDOUT, timeout=5)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()
    except subprocess.TimeoutExpired as e:
        return "Ping request timed out"

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid host name"}
    try:
        output = _execute_command(['ping', shlex.quote(host)])
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "failed", "error": str(e)}