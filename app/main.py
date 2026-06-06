from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '_', '-'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_input(host))
    # Safer implementation using shlex to split command safely
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}