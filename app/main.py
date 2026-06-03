from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('-', '.', '_'))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(shlex.split(f"ping {sanitized_host}"), check=True, capture_output=True)
    return {
        "status": "completed",
        "output": result.stdout.decode()
    }