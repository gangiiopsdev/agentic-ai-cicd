from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return input_string.strip()

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        # Use a safe list of arguments to avoid shell injection
        output = subprocess.check_output(['ping', '-c', '1', quote(sanitized_host)], timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}