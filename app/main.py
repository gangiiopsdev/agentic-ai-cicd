from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_value):
    return ''.join(e for e in input_value if e.isalnum() and not e.isdigit())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "error", "message": "Invalid input for host"}
    subprocess.call(shlex.split(f'ping {sanitized_host}'))
    return {"status": "completed"}