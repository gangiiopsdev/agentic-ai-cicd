from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(char if char.isalnum() else '_' for char in input_string)

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    safe_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', quote(safe_host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e.output)}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "message": "Ping timed out"}